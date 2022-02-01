import Dynamic_equations as dyneq
import solverFunctions as solver
import dataFormatting as dataForm
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

t,variables_out=solver.solveODEshift(t1,t2,N=np.array([0.05,0.5]))
T,tau,R,Pi=dataForm.variables_out_to_tauTRPi(variables_out)
dataForm.rawDataToTextFile(t,T,tau,R,Pi)









