#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:14:06 2022

@author: jose
"""
import numpy as np

# INPUTS
N = 0.5
O = 0
M = 0
I = 0
gamma = 1
mu = 1
xi = 7
Ro = 8
kPitoR = 9
Rstarved = 10
Pio = 11
delta = 12

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