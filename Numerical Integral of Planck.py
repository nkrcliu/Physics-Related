from scipy import integrate
from matplotlib import pyplot as plt
import numpy as np
import math

x = np.linspace(0.000001,100,1000)
y = np.sqrt(x)/(np.exp(x)-1)

plt.plot(x, y)
plt.show()

def func(t):
    return (t**0.5/(math.exp(t)-1))

FArea, err = integrate.quad(func,0.000001,700)
print(FArea)
