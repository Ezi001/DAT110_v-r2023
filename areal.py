# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:44:48 2023

@author: esthe
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

# Defining x an y values following the normal distribution
xs = np.arange(-4,4,1/40)
ys = norm.pdf(xs, 0, 1)

# Creating the figure
fig, ax = plt.subplots(1,1)
# Plot the curve
ax.plot(xs, ys)

# Fill under curve
ax.fill_between(
    x=xs,
    y1=ys,
    where= (-2<xs)&(xs<2),
    color="b",
    alpha=0.2)

area = norm.cdf(xs, 0, 1)


# Show
plt.show()