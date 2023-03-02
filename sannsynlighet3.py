# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:32:36 2023

@author: esthe
"""
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
mu = 0
sigma = 1
cut_off = -1.35

def normcdf(mu, sigma, cut_off):
    area = scipy.stats.norm.cdf(mu, sigma, cut_off)
    return area

def normpdf(mu, sigma, cut_off):
    val = scipy.stats.norm.cdf(mu, sigma, cut_off)
    return val

def sannsynlighet(cut_off, mu, sigma):
    area = normcdf(mu, sigma, cut_off)
    x = np.arange((mu-3)/sigma,(mu+3)/sigma, 0.001)
    # 
    fig = plt.figure(figsize=(5,6))
    plt.plot(x, scipy.stats.norm.pdf(x,mu,sigma))
    
    plt.plot(x[:cut_off], scipy.stats.norm.cdf(x[:cut_off],mu,sigma))
    
    plt.show()
    return areal2, fig

sannsynlighet(-1.35, 0, 1)

print(areal2)
#fig.show()