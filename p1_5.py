# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:31:55 2019

@author: pesimp23
"""

import numpy as np

x=0
h=0.1
ffp=(np.exp(x+h)-np.exp(x))/h
fcp=(np.exp(x+h)-np.exp(x-h))/(2*h)
effp=1-ffp
efcp=1-fcp
#%%
h=0.01
ffp=(np.exp(x+h)-np.exp(x))/h
fcp=(np.exp(x+h)-np.exp(x-h))/(2*h)
effp=1-ffp
efcp=1-fcp
#%%
h=0.001
ffp=(np.exp(x+h)-np.exp(x))/h
fcp=(np.exp(x+h)-np.exp(x-h))/(2*h)
effp=1-ffp
efcp=1-fcp
#%%
h=.1
fcpp=(np.exp(x+h)-2*np.exp(x)+np.exp(x-h))/h**2
efcpp=fcpp-1
#%%
h=.01
fcpp=(np.exp(x+h)-2*np.exp(x)+np.exp(x-h))/h**2
efcpp=fcpp-1
#%%
h=.001
fcpp=(np.exp(x+h)-2*np.exp(x)+np.exp(x-h))/h**2
efcpp=fcpp-1
#%%
h=1*10**-15
g=1+h
print(g-1)