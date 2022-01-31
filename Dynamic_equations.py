#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:14:06 2022

@author: jose
"""

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


# DEDUCED VARIABLES

def dT_dt(T,tau,R,Pi):
    return(gamma - mu - mu*T)

def dtau_dt(T,tau,R,Pi):
    return(mu - gamma + mu*xi*Ro*kPitoR/(kPitoR + Pi) - mu*tau)

def dR_dt(T,tau,R,Pi):
    return(mu*Ro*(kPitoR/kPitoR + Pi) - mu*R)

def dPi_dt(T,tau,R,Pi):
    return(Pio*Rstarved + O-(delta + M)*Pi)