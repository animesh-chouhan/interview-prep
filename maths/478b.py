# https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly
# http://www.anderswallin.net/2009/05/uniform-random-points-in-a-circle-using-polar-coordinates/
# https://stackoverflow.com/questions/1841014/uniform-random-monte-carlo-distribution-on-unit-sphere
# https://mathworld.wolfram.com/SpherePointPicking.html

import math
from random import uniform, choice
import matplotlib.pyplot as plt
import numpy as np

description = "asd"


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
        global description
        description = "• Naive approach"
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
        global description
        description = "• Random constrained approach"
        return [x, y]

    # # sqrt
    # def randPoint(self) -> list[float]:
    #     theta = uniform(0, 2 * math.pi)
    #     R = math.sqrt(uniform(0, self.radius**2))
    #     global description
    #     description = "• Probabilistic distribution approach"
    #     return [
    #         self.x_center + R * math.cos(theta),
    #         self.y_center + R * math.sin(theta),
    #     ]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
radius = 5
s = Solution(radius, 0, 0)


# https://matplotlib.org/stable/plot_types/basic/plot.html
plt.style.use("_mpl-gallery")

# make data
iterations = 20000
x = []
y = []
for i in range(iterations):
    p = s.randPoint()
    x.append(p[0])
    y.append(p[1])

r = [math.sqrt(a**2 + b**2) for a, b in zip(x, y)]

# plot
s = [1] * len(x)
fig, ax = plt.subplots(1, 2, layout="constrained", figsize=(14, 6))
fig.set_constrained_layout_pads(w_pad=0.8, h_pad=0.9)
ax[0].scatter(x, y, s, color="black")

lim = (-radius * 1.2, radius * 1.2)
ax[0].set(xlim=lim, xticks=np.arange(*lim), ylim=lim, yticks=np.arange(*lim))
ax[0].set(aspect=1)
# ax[0].axis("equal")

circle = plt.Circle((0, 0), radius, color="black", fill=False)
ax[0].add_patch(circle)


binwidth = 0.1
lim = (int(np.max(r) / binwidth) + 1) * binwidth
bins = np.arange(-lim, lim + binwidth, binwidth)
ax[1].hist(r, bins=bins, density=False, edgecolor="white", color="black")
ax[1].set(
    xlim=(0, radius),
    xticks=np.arange(0, radius + binwidth, binwidth * 2),
    ylim=(0, 1000),
    yticks=np.linspace(0, 1000, 11),
)
ax[1].set_aspect(np.diff(ax[1].get_xlim())[0] / np.diff(ax[1].get_ylim())[0])
# ax[1].set(aspect=1)

fig.suptitle(description, y=0.04, ha="center", fontsize="xx-large", fontweight="bold")
# plt.subplots_adjust(bottom=0.1, right=0.72, left=0.28, top=0.9)
mng = plt.get_current_fig_manager()
mng.resize(1920, 1080)
plt.show()
