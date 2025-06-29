import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader, random_split
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score



# ----------------------
# Dataset
# ----------------------
class HeightMapRegressionDataset(Dataset):
    def __init__(self, directory):
        self.files = glob.glob(os.path.join(directory, "*.csv"))

    def __len__(self):
        return len(self.files)
    
    

    def __getitem__(self, idx):
        filepath = self.files[idx]
        data = np.loadtxt(filepath, delimiter=",", dtype=np.float32)

        rows, cols = data.shape
        TARGET_ROWS=64
        if rows > TARGET_ROWS:
            data = data[:TARGET_ROWS, :]
        elif rows < TARGET_ROWS:
            if rows == 0:
                pad = np.zeros((TARGET_ROWS, cols))
                data = pad
            else:
                last_row = data[-1, :][np.newaxis, :]
                pad = np.repeat(last_row, TARGET_ROWS - rows, axis=0)
                data = np.vstack([data, pad])

        data = (data - np.mean(data)) / (np.std(data) + 1e-6)
        data = data[np.newaxis, :, :]  # Shape: (1, H, W)

        score = float(filepath.split("_score_")[1].replace(".csv", ""))
        return torch.tensor(data, dtype=torch.float32), torch.tensor(score, dtype=torch.float32)

# ----------------------
# CNN Model
# ----------------------
class HeightMapRegressor(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1), nn.BatchNorm2d(16), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(), nn.AdaptiveAvgPool2d((1, 1))
        )
        self.regressor = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64, 64), nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.regressor(self.features(x)).view(-1)
    
    def get_feature_maps(self, x):
        return self.features(x)
    
    def forward_debug(self, x):
        out1 = self.features[0](x)  # Conv2d
        out2 = self.features[1](out1)  # BatchNorm
        out3 = self.features[2](out2)  # ReLU
        out4 = self.features[3](out3)  # MaxPool
        return [out1, out2, out3, out4]

# ----------------------
# Training Setup
# ----------------------

# ----------------------
# Training Loop
# ----------------------



def main():   
    N_EPOCHS=100
    LEARNING_RATE= 1e-3 
    dataset = HeightMapRegressionDataset("scanned_maps")
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=16, shuffle=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = HeightMapRegressor().to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)



    for epoch in range(1, N_EPOCHS+1):
        # if epoch > 30:
        #     LEARNING_RATE=2e-4

        model.train()
        total_loss = 0.0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            preds = model(xb)
            loss = criterion(preds, yb)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        # Validation
        model.eval()
        val_loss = 0.0
        all_preds = []
        all_targets = []
        with torch.no_grad():
            for xb, yb in val_loader:
                xb, yb = xb.to(device), yb.to(device)
                preds = model(xb)
                val_loss += criterion(preds, yb).item()
                all_preds.append(preds.cpu().numpy())
                all_targets.append(yb.cpu().numpy())
        # Flatten arrays
        all_preds = np.concatenate(all_preds)
        all_targets = np.concatenate(all_targets)

        rmse = np.sqrt(val_loss / len(val_loader))
        r2 = r2_score(all_targets, all_preds)

        print(f"Epoch {epoch} | Train Loss: {total_loss / len(train_loader):.4f} | "
              f"Val Loss: {val_loss / len(val_loader):.4f} | RMSE: {rmse:.4f} | R2: {r2:.4f}")

    # ----------------------
    # Save Model
    # ----------------------
    torch.save(model.state_dict(), "heightmap_regressor.pth")
    print("✅ Model saved as 'heightmap_regressor.pth'")


if __name__=="__main__":
    main()
