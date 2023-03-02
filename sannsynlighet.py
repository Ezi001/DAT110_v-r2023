# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:29:10 2023

@author: esthe
"""

import scipy.stats as ss
import numpy as np

n = 120
p = 0.9
mu = 108
x = 105

sigma = np.sqrt(n*p*(1-p))

# standardised z-score

z = ((x+0.5) - mu)/sigma

# Bruker Normalfordelingen som approksimasjon

p = ss.norm.cdf(z)
