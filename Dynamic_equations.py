#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:14:06 2022

@author: jose
"""
import numpy as np

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