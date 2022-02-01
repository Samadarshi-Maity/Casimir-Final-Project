#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:14:06 2022

@author: jose
"""
import numpy as np
import math
import scipy.integrate as spint

# INPUTS
xi = 0.350335
kTOnMu = 0.001377
kTauOnGamma = 0.000176
muMax = 6.732008
gammaMax = 61.337662
Rmax = 0.281656
Ro = 1.820228
kPitoR = 2.345878
delta = 18.092349
Pi0 = 47053.186045
# DEDUCED VARIABLES

def rates(Variables,t,I=0,M=0,N=0,O=0):
    """
    This function represent the set of differential equations to that wil
    be solved.
    Input:
        Variables: T,tau,R, Pi
    Output:
        
    """
    T = Variables[0]
    tau = Variables[1]
    R = Variables[2]
    Pi = Variables[3]
    
    gamma = gammaMax*N*(Rmax-R)*tau/(tau+kTauOnGamma)
    mu = muMax*R*(1 - I)*(T/(T + kTOnMu))
    Rstarved = kTOnMu/(kTOnMu + T)
    dT_dt = gamma - mu - mu*T
    dtau_dt = mu - gamma + mu*xi*Ro*kPitoR/(kPitoR + Pi) - mu*tau
    dR_dt = mu*Ro*(kPitoR/kPitoR + Pi) - mu*R
    dPi_dt = Pi0*Rstarved + O-(delta + M)*Pi
    return [dT_dt,dtau_dt,dR_dt,dPi_dt]

def solveODEconstantInputs(t1,t2,variables0,I=0,M=0,N=0,O=0,dt=0.01):
    '''Solves ODE between t1 and t2 for constant inputs I,M,N,O'''
    
    nPts=math.floor((t2-t1)/dt)
    t=np.linspace(t1,t2,nPts)
    
    rates_function = lambda variables,t : rates(variables,t,I,M,N,O)
    variables_out=spint.odeint(rates_function,variables0,t)
    
    return (t,variables_out)

def growth_rate(T,R,I=0):
    mu = muMax*R*(1 - I)*(T/(T + kTOnMu))
    return(mu)

def solveODEshift(t1,t2,variables0,I,M,N,O,dt=0.01):
    I_init = I[0]
    M_init = M[0]
    N_init = N[0]
    O_init = O[0]
    t_before,variables_out = solveODEconstantInputs(t1,0,variables0,
                                         I_init,M_init,N_init,O_init,dt=0.01)
    T_before=variables_out.T[0]
    tau_before=variables_out.T[1]
    R_before=variables_out.T[2]
    Pi_before=variables_out.T[3]
    I_end = I[1]
    M_end = M[1]
    N_end = N[1]
    O_end = O[1]
    variables0 = [T_before[-1],tau_before[-1],R_before[-1],Pi_before[-1]]
    t_after, variables_out = solveODEconstantInputs(0,t2,variables0,I_end,
                                                    M_end,N_end,O_end,dt=0.01)
    T_after=variables_out.T[0]
    tau_after=variables_out.T[1]
    R_after=variables_out.T[2]
    Pi_after=variables_out.T[3]
    
    t = np.array([*t_before,*t_after])
    T = np.array([*T_before,*T_after])
    tau = np.array([*tau_before,*tau_after])
    R = np.array([*R_before,*R_after])
    Pi = np.array([*Pi_before,*Pi_after])
    return(T,tau,R,Pi,t)    
