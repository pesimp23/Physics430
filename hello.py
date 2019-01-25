import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt

x=np.arange(0,10,0.01)
y=np.sin(5*x)

plt.figure()
plt.plot(x,y,'ro')
plt.show()
plt.savefig('filename.png')
plt.scatter(x,y)
nhalf=len(x)/2
plt.plot(x[0:nhalf],y[0:nhalf])
plt.plot(x[nhalf:],y[nhalf:])
plt.show()