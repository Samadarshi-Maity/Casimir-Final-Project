#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:14:06 2022

@author: jose
"""
import numpy as np

# INPUTS
N = 0
O = 0
M = 0
I = 0
gamma = 0
mu = 0
xi = 0
Ro = 0
kPitoR = 0
Rstarved = 0
Pio = 0
delta = 0
tmax = 20
t = np.linspace(0,tmax,0.01)

# DEDUCED VARIABLES

def rates(Variables,t):
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
    
    dT_dt = gamma - mu - mu*T
    dtau_dt = mu - gamma + mu*xi*Ro*kPitoR/(kPitoR + Pi) - mu*tau
    dR_dt = mu*Ro*(kPitoR/kPitoR + Pi) - mu*R
    dPi_dt = Pio*Rstarved + O-(delta + M)*Pi
    return [dT_dt,dtau_dt,dR_dt,dPi_dt]