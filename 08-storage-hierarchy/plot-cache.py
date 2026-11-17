#!/usr/bin/python3

import numpy as np
from PIL import Image
import matplotlib
import os

matplotlib.use("Agg")

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "TakaoPGothic"


def plot_cache():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x, y = np.loadtxt("out.txt", unpack=True)
    ax.scatter(x, y, s=1)
    ax.set_title("Visualizing the effect of cache memory")
    ax.set_xlabel("Buffer size [2^x KiB]")
    ax.set_ylabel("Access rate [accesses/ns]")

    # Work around a matplotlib bug in Ubuntu 20.04 by saving as PNG before converting to JPG.
    # https://bugs.launchpad.net/ubuntu/+source/matplotlib/+bug/1897283?comments=all
    pngfilename = "cache.png"
    jpgfilename = "cache.jpg"
    fig.savefig(pngfilename)
    Image.open(pngfilename).convert("RGB").save(jpgfilename)
    os.remove(pngfilename)


plot_cache()
