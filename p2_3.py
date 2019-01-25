# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:53:43 2019

@author: pesimp23
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import scipy.special as sps

#%% a
N=30
a=0
b=5
x,h=np.linspace(a,b,N,retstep=True)

y=-4*sps.jn(1,x)/sps.jn(1,5)+x

A=np.zeros((N,N))

for i in range(1,N-1):
    A[i][i]=-2/h**2+1-1/x[i]**2
    A[i][i-1]=1/h**2-1/(2*h*x[i])
    A[i][i+1]=1/h**2+1/(2*h*x[i])
A[0][0]=1
A[N-1][N-1]=1

B=np.copy(x)
B[0]=0
B[-1] = 1

Y=la.solve(A,B)

plt.figure()
plt.plot(x,y,'b')
plt.plot(x,Y,'r.')
plt.show()

#%% b
N=20001 #this is how many points you have to use to get 3-digit accuracy
a=0
b=5
x,h=np.linspace(a,b,N,retstep=True)

A=np.zeros((N,N))

for i in range(1,N-1):
    A[i][i]=-2/h**2+np.exp(x[i])
    A[i][i-1]=1/h**2-np.sin(x[i])/(2*h)
    A[i][i+1]=1/h**2+np.sin(x[i])/(2*h)
A[0][0]=1
A[N-1][N-1]=1

B=x**2
B[0]=0
B[-1]=3

y=la.solve(A,B)

plt.figure()
#plt.plot(x,y,'b')
plt.plot(x,y,'r')
plt.show()
j=int(4.5/h)
print(y[j])