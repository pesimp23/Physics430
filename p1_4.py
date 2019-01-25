# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt

N=20
x,h=np.linspace(0,5,N,retstep=True)
f=sps.jn(0,x)
fp=np.zeros_like(f)
fp[1:N-1]=(f[2:N]-f[0:N-2])/(2*h)
fpp=np.zeros_like(f)
fpp[1:N-1]=(f[2:N]-2*f[1:N-1]+f[0:N-2])/h**2
fp[0]=2*fp[1]-fp[2]
fp[N-1]=2*fp[N-2]-fp[N-3]
fpp[0]=2*fpp[1]-fpp[2]
fpp[N-1]=2*fpp[N-2]-fpp[N-3]

plt.figure()
plt.plot(x,f)
plt.plot(x,fp)
plt.plot(x,fpp)
plt.plot(x,-sps.jn(1,x))
plt.plot(x,1/2*(-sps.jn(0,x)+sps.jn(2,x)))
plt.show()