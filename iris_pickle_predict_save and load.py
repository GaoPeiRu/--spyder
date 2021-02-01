# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:51:31 2021

@author: T30518
"""

import pickle

pkl_filename= "iris_model.pkl" 
with  open(pkl_filename, 'rb') as file:
    pickle_model= pickle.load(file)

newX= [[7.7, 2.6, 3.2, 2.2],[3.1, 3.2, 4.8, 1.8]] 
print(pickle_model.predict(newX))