# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:22:17 2023

@author: esthe
"""

import matplotlib.pyplot as plt
from scipy.stats import binom

# Setting values of n and p
n = 6
p = 0.6

# Definerer liste av r verdier
r_verdier = list(range(n + 1))

# Liste av pmf verdier
dist = [binom.pmf(r, n, p) for r in r_verdier]

# Plotter grafen
plt.bar(r_verdier, dist)
plt.show()