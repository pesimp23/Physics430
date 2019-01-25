# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:16:39 2019

@author: pesimp23
"""
import matplotlib.pyplot as plt
import numpy as np

#%% (a)
N=100
a=0
b=np.pi
x,h=np.linspace(a,b,N,retstep=True)
y=np.sin(x)*np.sinh(x)
plt.figure()
plt.plot(x,y)
plt.show()

#%% (b)
h=2/100
x=np.arange(h/2,2,h)
f=np.cos(x)
plt.figure()
plt.plot(x,f)
plt.show()
print(sum(f)*h)
print(np.sin(2))

#%% (c)
h=np.pi/2/500
x=np.arange(-h/2,np.pi/2+3*h/2,h)
f=np.sin(x)