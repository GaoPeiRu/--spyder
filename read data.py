# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:00:08 2021

@author: T30518
"""
from sklearn.preprocessing import LabelEncoder
names = ['age','sex','region','income','married','children','car','sa ve_act','current_act','mortgage','pep'] 
dataset = pd.read_csv('bank-data.csv', names=names)
X = dataset.drop('pep', axis=1)  
y = dataset['pep']

Labelencoder=LabelEncoder()

X_le=X
X_le['sex']=labelencoder.fit_transform(X_Le['sex'])

