# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:27:36 2021

@author: T30518
"""
from sklearn.datasets import load_iris 
from sklearn import tree 
from sklearn.model_selection import cross_val_score
from sklearn.tree import export_text
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, classification_report
import pickle


iris = load_iris() 
X = iris.data 
y = iris.target 
clf= tree.DecisionTreeClassifier() 
clf= clf.fit(X, y) 
score = cross_val_score(clf, X, y, cv=10, scoring='accuracy')

pkl_filename= "iris_model.pkl" 
with  open(pkl_filename, 'wb') as file:#寫二進制文件 pickle.dump(model, file)
    pickle.dump(clf, file)

print(score) 
print("%0.2f accuracy with a standard deviation of %0.2f" % (score.mean(), score.std()))
tree_rules= export_text(clf, feature_names=iris['feature_names']) 
print(tree_rules)
y_pred= cross_val_predict(clf, X, y, cv=10) 
conf_mat= confusion_matrix(y, y_pred)

print(confusion_matrix(y, y_pred)) 
print(classification_report(y, y_pred))
