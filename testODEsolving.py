import Dynamic_equations as dyneq
import scipy.integrate as spint
import numpy as np
import matplotlib
matplotlib.style.use('classic')
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)

tmax = 1
nPts=100
t=np.linspace(0,tmax,nPts)

T_init=0.1
tau_init=0.2
R_init=0.15
Pi_init=10
variables0 = np.array([T_init,tau_init,R_init,Pi_init])

t_init = -2.5
t_end = 3
I = [0,0]
M = [1,1]
N = [0.5,2]
O = [1,1]
T,tau,R,Pi,t = dyneq.solveODEshift(t_init,t_end,variables0,I,M,N,O)
mu = dyneq.growth_rate(T,R)
plt.plot(t,mu)


