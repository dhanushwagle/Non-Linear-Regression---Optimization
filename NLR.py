# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:19:23 2021

@author: Dhanush Wagle
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y = np.array([2.86, 2.64, 1.57, 1.24, 0.45, 1.02, 0.65, 0.18, 0.15, 0.01, 0.04, 0.36])
x = np.array([0.0, 0.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0])

def nlr(x,b1,b2,b3):
    return b1+b2*np.exp(-b3*x)

g = [1.0,2.0,1.0]

n = len(x)
y_pred = np.empty(n)
y_pred1 = np.empty(n)
i,j=0,0

for values in x:
    y_pred[i] = nlr(values,g[0],g[1],g[2])
    i+=1

c,cov = curve_fit(nlr,x,y)
print(c)

for values in x:
    y_pred1[j] = nlr(values,c[0],c[1],c[2])
    j+=1
    
print(y_pred)
print(y_pred1)

plt.plot(x,y_pred,'r-',label='guess')
plt.plot(x,y_pred1,'g-',label='optimized')
plt.plot(x,y,'bo',label='real')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
#plt.savefig('nrl.jpeg', dpi=300)
plt.show()



