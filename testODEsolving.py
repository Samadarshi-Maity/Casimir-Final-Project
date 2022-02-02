import Dynamic_equations as dyneq
import scipy.integrate as spint
import numpy as np
import matplotlib
matplotlib.style.use('classic')
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)


T_init=0.1
tau_init=0.2
R_init=0.15
Pi_init=10
variables0 = np.array([T_init,tau_init,R_init,Pi_init])

t_init = -100
t_end = 3
I = [0.0,0.0]
M = [0.0,0.0]
N = [0.001,0.5]
O = [0.0,0.0]
T,tau,R,Pi,t = dyneq.solveODEshift(t_init,t_end,variables0,I,M,N,O)
Iarray = np.ones(len(T))*I[0]
index = np.where(t==0)
Iarray[index[0][0]:] = I[1]
mu = dyneq.growth_rate(T,R,Iarray)
plt.plot(t,mu)
plt.xlim(-2.5,3)
plt.ylim(0,1)
plt.axvline(x=0,color = 'grey',linestyle='--')
plt.xlabel('t',fontsize = 20)
plt.ylabel(r'$\mu$',fontsize = 20)


