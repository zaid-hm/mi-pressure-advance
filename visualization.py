# import cv2
import numpy as np
import matplotlib.pyplot as plt
from pa_result import PaResult
from pathlib import Path

from constants import *

def generate_color_map(pa_result: PaResult,title="Height Map"):
    fig, ax = plt.subplots()

    x = np.arange(len(pa_result.height_data))
    y = np.arange(len(pa_result.height_data[0]))
    (x ,y) = np.meshgrid(x,y)

    c = ax.pcolormesh(x, y, np.transpose(pa_result.height_data), cmap='plasma')
    fig.colorbar(c)
    ax.set_xlabel("X Value (Frame)")
    ax.set_ylabel("Y Value (Pixel)")

    ax.set_title(title, fontsize=10)
    return fig


def generate_3d_height_map(pa_result: PaResult,title="3D Height Map"):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    y = np.arange(len(pa_result.height_data))
    x = np.arange(len(pa_result.height_data[0]))
    (x ,y) = np.meshgrid(x,y)
    ax.plot_surface(x, y, pa_result.height_data, cmap="plasma")
    ax.set_zlim3d(10, 50)

    ax.set_ylabel("X Value (Frame)")
    ax.set_xlabel("Y Value (Pixel)")
    ax.set_zlabel("Height")

    ax.set_title(title, fontsize=10, y=1)
    
    fig.tight_layout()

    return fig



