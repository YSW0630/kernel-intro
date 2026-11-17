#!/usr/bin/python3

import numpy as np
from PIL import Image
import matplotlib
import os

matplotlib.use("Agg")

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "TakaoPGothic"


def plot_sched(concurrency):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for i in range(concurrency):
        x, y = np.loadtxt("{}.data".format(i), unpack=True)
        ax.scatter(x, y, s=1)
    ax.set_title("Visualizing time slices (concurrency = {})".format(concurrency))
    ax.set_xlabel("Elapsed time [ms]")
    ax.set_xlim(0)
    ax.set_ylabel("Progress [%]")
    ax.set_ylim([0, 100])
    legend = []
    for i in range(concurrency):
        legend.append("Workload " + str(i))
    ax.legend(legend)

    # Work around a matplotlib bug in Ubuntu 20.04 by saving as PNG before converting to JPG.
    # https://bugs.launchpad.net/ubuntu/+source/matplotlib/+bug/1897283?comments=all
    pngfilename = "sched-{}.png".format(concurrency)
    jpgfilename = "sched-{}.jpg".format(concurrency)
    fig.savefig(pngfilename)
    Image.open(pngfilename).convert("RGB").save(jpgfilename)
    os.remove(pngfilename)
