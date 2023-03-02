# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:19:04 2023

@author: esthe
"""

from numpy.random import seed
from numpy.random import normal

# Reproducible sample
seed(1)

# Generate sample of 200 vals that follow a normal distribution
data = normal(loc=0, scale=1, size=200)

# View first six vals
data[0:5]

import numpy as np
np.mean(data)

np.std(data, ddof=1)

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(data, 30)
plt.show()
