import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os
import csv

# Parameters
width = 128
height = 64
min_height = 16
center_y = height // 2
output_dir = "generated_maps"
num_maps = 500


# Create output directory
os.makedirs(output_dir, exist_ok=True)

def generate_height_map(score):

    # Initialize the height map
    height_map = np.full((height, width), min_height, dtype=np.float32)

    # Randomize section widths
    narrow_start = np.random.randint(22, 27)
    narrow_width = np.random.randint(8, 14)
    narrow_end = narrow_start + narrow_width

    wide_start = np.random.randint(88,93)
    wide_width = np.random.randint(18, 26)
    wide_end = wide_start + wide_width

    # score= np.random.rand()
    print(score)
    # Iterate over each column
    for x in range(width):
        # Determine section and assign parameters
        if narrow_start <= x <= narrow_end:
            std=2-1.6*(1-score)
            max_h = np.random.uniform(25, 28)-10*(1-score)

        elif wide_start <= x <= wide_end:
            std=2+2*(1-score)
            max_h = np.random.uniform(23, 25)+10*(1-score)

        else:
            std = np.random.uniform(1.9, 2.1)
            max_h = np.random.uniform(25, 28)

        # Gaussian profile
        y = np.arange(height)
        gaussian = norm.pdf(y, loc=center_y, scale=std)
        gaussian /= gaussian.max()  # Normalize to 1

        # Scale to [min_height, max_h]
        height_column = min_height + gaussian * (max_h - min_height)
        height_map[:, x] = height_column

    return height_map,score

def plot_height_map(height_map):
    plt.figure(figsize=(6, 4))
    plt.imshow(height_map, aspect='auto', cmap='plasma')
    plt.colorbar()
    plt.title("Height Map with Randomized Sections")
    plt.xlabel("X (Frame)")
    plt.ylabel("Y (Pixel)")
    plt.tight_layout()
    plt.show()
    return


def main():
    # for i in range(num_maps):
    #     if i < num_maps//2:
    #         score=np.random.uniform(0.9, 1)
    #     else:
    #         score=np.random.uniform(0, 0.6)
    #     height_map, score = generate_height_map(score)
    #     filename = f"map_{i:03d}_score_{score:.4f}.csv"
    #     filepath = os.path.join(output_dir, filename)
    #     np.savetxt(filepath, height_map, delimiter=",")
    height_map, score = generate_height_map(0.3)
    plot_height_map(height_map)
    print(score)


if __name__ == "__main__":
    main()