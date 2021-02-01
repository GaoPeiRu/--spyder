# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:58:12 2021

@author: T30518
"""



import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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

reg= LinearRegression() 
reg.fit(X, y) 
print(u'係數', reg.coef_) 
print (u'截距', reg.intercept_) 
print (u'評分函式', reg.score(X, y))
X2 = [[1], [10], [14], [25]] 
y2 = reg.predict(X2)
print(y2)

X2 = [[1], [10], [14], [25]] 
y2 = reg.predict(X2) 
print(y2) 

plt.figure() 
plt.title('Pizza Price with diameter.') 
plt.xlabel('diameter(inch)') 
plt.ylabel('price($)') 
plt.axis([0, 25, 0, 25]) 
plt.grid(True) 
plt.plot(X, y, 'k.') 
plt.plot(X2, y2, '-g.') 