import math
from random import uniform, choice
import matplotlib.pyplot as plt
import numpy as np


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    # wrong
    def randPoint(self) -> list[float]:
        r = uniform(0, self.radius)
        theta = 2 * math.pi * uniform(0, 1)
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]

    # square
    def randPoint(self) -> list[float]:
        while True:
            rand_y = uniform(-self.radius, self.radius)
            rand_x = uniform(-self.radius, self.radius)
            if rand_x**2 + rand_y**2 <= self.radius**2:
                break
        x = self.x_center + rand_x
        y = self.y_center + rand_y
        return [x, y]

    # sqrt
    def randPoint(self) -> list[float]:
        theta = uniform(0, 2 * math.pi)
        R = math.sqrt(uniform(0, self.radius**2))
        return [
            self.x_center + R * math.cos(theta),
            self.y_center + R * math.sin(theta),
        ]

    #
    def randPoint(self) -> list[float]:
        x = uniform(0, 2 * math.pi)
        R = math.sqrt(uniform(0, self.radius**2))
        return [
            self.x_center + R * math.cos(theta),
            self.y_center + R * math.sin(theta),
        ]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
radius = 5
s = Solution(radius, 0, 0)


plt.style.use("_mpl-gallery")

# make data
x = []
y = []
for i in range(20000):
    p = s.randPoint()
    x.append(p[0])
    y.append(p[1])


# # plot
# s = [1] * len(x)
# fig, ax = plt.subplots()
# ax.scatter(x, y, s)

# lim = (-radius * 1.2, radius * 1.2)
# ax.set(xlim=lim, xticks=np.arange(*lim), ylim=lim, yticks=np.arange(*lim))
# # ax.axis("equal")

# circle = plt.Circle((0, 0), radius, color="r", fill=False)
# ax.add_patch(circle)

# plt.subplots_adjust(bottom=0.1, right=0.72, left=0.28, top=0.9)
# mng = plt.get_current_fig_manager()
# mng.resize(1920, 1080)
# plt.show()


# https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#sphx-glr-gallery-lines-bars-and-markers-scatter-hist-py
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    s = [1] * len(x)
    # the scatter plot:
    ax.scatter(x, y, s, color="black")
    circle = plt.Circle((0, 0), radius, color="r", fill=False)
    ax.add_patch(circle)

    # now determine nice limits by hand:
    binwidth = 0.1
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax / binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins, density=True, edgecolor="white", color="black")
    ax_histy.hist(
        y,
        bins=bins,
        orientation="horizontal",
        density=True,
        edgecolor="white",
        color="black",
    )


# fig = plt.figure()
# gs = fig.add_gridspec(
#     2,
#     2,
#     width_ratios=(4, 1),
#     height_ratios=(1, 4),
#     left=0.1,
#     right=0.9,
#     bottom=0.1,
#     top=0.9,
#     wspace=0.05,
#     hspace=0.05,
# )

# # Create the Axes.
# ax = fig.add_subplot(gs[1, 0])
# ax.set(aspect=1)
# ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
# ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
# # Draw the scatter plot and marginals.
# scatter_hist(x, y, ax, ax_histx, ax_histy)

# Create a Figure, which doesn't have to be square.
fig = plt.figure(layout="constrained")
fig.set_constrained_layout_pads(w_pad=0.8, h_pad=0.5)
# Create the main axes, leaving 25% of the figure space at the top and on the
# right to position marginals.
ax = fig.add_gridspec(
    top=0.5,
    right=0.75,
    bottom=0.3,
    wspace=0.01,
    hspace=0.08,
).subplots()
# The main axes' aspect can be fixed.
ax.set(aspect=1)

ax_histx = ax.inset_axes([0, 1.05, 1, 0.25], sharex=ax)
ax_histy = ax.inset_axes([1.05, 0, 0.25, 1], sharey=ax)
# Draw the scatter plot and marginals.
scatter_hist(x, y, ax, ax_histx, ax_histy)

# plt.subplots_adjust(bottom=0.2, right=0.72, left=0.28, top=0.8)
mng = plt.get_current_fig_manager()
mng.resize(1500, 1000)
plt.show()
