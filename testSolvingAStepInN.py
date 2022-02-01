import Dynamic_equations as dyneq
import solverFunctions as solver
import scipy.integrate as spint
import numpy as np

N1=0.2
N2=0.6

t_steadyStateFinding=-10
t1=-1
t2=3

T_init=0.1
tau_init=0.2
R_init=0.15
Pi_init=10

variables_out1,t1=solver.solveODEconstantInputs(t1,0,[T_init,tau_init,R_init,Pi_init],N=0.2)
variables_out2,t2=solver.solveODEconstantInputs(0,t2,variables_out1[-1,:],N=0.5)

variables_out=np.concatenate((variables_out1,variables_out2))