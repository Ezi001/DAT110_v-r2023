# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:32:36 2023

@author: esthe
"""
import scipy.stats
# Definerer 
Cut_off = 1.35

# Beregner arealet under kurven der Z < cut_off.
areal = scipy.stats.norm.cdf(0.5)
areal2 = 1-scipy.stats.norm.cdf(8)
a = areal2+areal
to_sidig = 2*areal


