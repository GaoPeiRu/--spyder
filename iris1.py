# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:45:54 2021

@author: T30518
"""

import seaborn as sns 

iris = sns.load_dataset('iris') 
iris.head() 
sns.set() 
sns.pairplot(iris, hue='species', size=3)

