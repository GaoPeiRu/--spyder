# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:56:59 2021

@author: T30518
"""

from sklearn.datasets import load_iris 
from sklearn import tree 
import graphviz
X, y = load_iris(return_X_y=True) 
clf= tree.DecisionTreeClassifier(min_samples_leaf=3) 
clf= clf.fit(X, y) 
tree.plot_tree(clf) 
