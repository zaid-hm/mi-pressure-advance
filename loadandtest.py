import os
import glob
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
from tqdm import tqdm



# ----------------------
# Model Definition
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

model =HeightMapRegressor().to('cuda')
model.load_state_dict(torch.load("heightmap_regressor_0.8.pth", map_location=torch.device('cuda')))
model.eval()

def selectValue(maps:list):
    best=0
    for i,map in enumerate(maps):
        with torch.no_grad():
            map=map.to('cuda')
            if model(map)>model(maps[best]):
                best=i
    return best,model(maps[best])



# ----------------------
# Process All Heightmaps
# ----------------------
input_dir = "scanned_maps"
threshold = 0.8
csv_files = sorted(glob.glob(os.path.join(input_dir, "*.csv")))
# print(csv_files)
i=0
correct=0
maps=[]
for j,filepath in enumerate(tqdm(csv_files)):

    data = np.loadtxt(filepath, delimiter=",", dtype=np.float32)
    rows, cols = data.shape
    if rows > 64:
            data = data[:64, :]
    elif rows < 64:
        if rows == 0:
            pad = np.zeros((64, cols))
            data = pad
        else:
            last_row = data[-1, :][np.newaxis, :]
            pad = np.repeat(last_row, 64 - rows, axis=0)
            data = np.vstack([data, pad])
    data = (data - np.mean(data)) / (np.std(data) + 1e-6)
    data = data[np.newaxis, :, :]  # Shape: (1, H, W)
    tensor = torch.tensor(data, dtype=torch.float32).to('cuda')
    tensor = tensor.unsqueeze(0) 
    
    # with torch.no_grad():
    #     pred=model(tensor)
    # true_score = float(filepath.split("_score_")[1].replace(".csv", ""))
    # print(f"true:{true_score}, predicted:{pred}")
    maps.append(tensor)
    if i>=9:
        n,score=selectValue(maps)
        true_score = float(csv_files[j-i+n].split("_score_")[1].replace(".csv", ""))
        if true_score>=0.9:
            correct+=1
            print(f"correct: {correct}")
        # else:
        #     print(f"pred:{score}, true:{true_score}")
        maps=[]
        i=-1
    i+=1

print(f"acc= {correct/8}")

