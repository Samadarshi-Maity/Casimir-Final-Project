import Dynamic_equations as dyneq
import scipy.integrate as spint
import numpy as np
import math

def solveODEconstantInputs(t1,t2,variables0,I=0,M=0,N=0,O=0,dt=0.01):
    '''Solves ODE between t1 and t2 for constant inputs I,M,N,O'''
    
    nPts=math.floor((t2-t1)/dt)
    t=np.linspace(t1,t2,nPts)
    
    rates = lambda variables,t : dyneq.rates(variables,t,N=1)
    variables_out=spint.odeint(rates,variables0,t)
    
    timeAndVariables_out=np.concatenate((t,variables_out))
    
    return variables_out

def solveODEshift(t1,t2,I=np.array([0,0]),M=np.array([0,0]),N=np.array([0,0]),O=np.array([0,0]),t_SS_finding=10,variables_SS_finding=[0.1,0.2,0.15,10]):
    '''Solves ODE between t1 and t2 for shift in inputs at t=0
    
    ___ Inputs ___
    t1: float<0
    t2: float>0
    I: numpy array of size 2, I[0] value of I before then shift, I[1] value of I after then shift
    M: same as above for M
    N: same as above for N
    O: same as above for O
    t_SS_finding: float, length of the simulation to reach and extract steady state, default value 10
    variables_SS_finding: float, variables starting point to reach and extract steady state, default value 10'''
    variables_out_SS_finding=solver.solveODEconstantInputs(t1,0,variables_SS_finding,N=0.2)
    variables_out1=solver.solveODEconstantInputs(t1,0,variables_out_SS_finding[-1,:],N=0.2)
    variables_out2=solver.solveODEconstantInputs(0,t2,variables_out1[-1,:],N=0.5)

    variables_out=np.concatenate((variables_out1,variables_out2))
    
    return variables_out

