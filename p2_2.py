# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:21:29 2019

@author: pesimp23
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la

N=30
a=0
b=2
x,h=np.linspace(a,b,N,retstep=True)

y=(16*np.sin(3*x)+np.cos(6-x)-np.cos(6+x)+np.cos(2+3*x)-np.cos(2-3*x))/(16*np.sin(6))

A=np.zeros((N,N))

for i in range(1,N-1):
    A[i][i]=-2/h**2+9
    A[i][i-1]=1/h**2
    A[i][i+1]=1/h**2
A[0][0]=1
A[N-1][N-1]=1

B=np.sin(x)
B[-1] = 1

Y=la.solve(A,B)

plt.figure()
plt.plot(x,y,'b')
plt.plot(x,Y,'r.')
plt.show()