import Dynamic_equations as dyneq
import scipy.integrate as spint
import numpy as np
import matplotlib
matplotlib.style.use('classic')
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)

tmax=1
nPts=100
t=np.linspace(0,tmax,nPts)

T_init=0.1
tau_init=0.2
R_init=0.15
Pi_init=10

rates = lambda variables,t : dyneq.rates(variables,t,N=1)
variables_out=spint.odeint(rates,[T_init,tau_init,R_init,Pi_init],t)


# ~~~~~~~~  Save the array into a text file ~~~~~~~~~~~~~
print('Saving the population arrray')
np.savetxt('populations.txt',variables_out, fmt = '%.2e')
#a_file = open("populations.txt", "w")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


T=variables_out[0]
tau=variables_out[1]
R=variables_out[2]
Pi=variables_out[3]


