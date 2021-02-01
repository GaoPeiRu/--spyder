# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:37:30 2021

@author: T30518
"""

import numpy as np 
import matplotlib.pyplot as plt

X = [[6], [8], [10], [14], [18]] #X是大寫
y = [[7], [9], [13], [17.5], [18]]
plt.figure() 
plt.title('Pizza Price with diameter.') 
plt.xlabel('diameter(inch)') 
plt.ylabel('price($)') 
plt.axis([0, 25, 0, 25]) 
plt.grid(True) 
plt.plot(X, y, 'k.') 
plt.show()
