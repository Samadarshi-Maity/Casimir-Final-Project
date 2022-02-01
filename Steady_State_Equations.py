# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 15:24:25 2022

@author: lion
"""
import numpy as np
from scipy.optimize import fsolve

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


def non_linear_solution(var_set, NOMI):
    
    ### Constants
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
    
    ### variables
    T    = var_set[0]
    tau  = var_set[1]
    R    = var_set[2]
    Pi   = var_set[3]
    
    # Arguments to vary 
    N = NOMI[0]
    O = NOMI[1]
    M = NOMI[2]
    I = NOMI[3]

    ### Set of equations
    gamma = N*(Rmax-R)*tau/(tau+kTauOnGamma)
    mu = muMax*R*(1 - I)*(T/(T + kTOnMu))
    a1 = gamma - mu - mu*T
    a2 = mu- gamma + mu*xi*Ro*kPitoR/(kPitoR + Pi) - mu*tau
    a3 = mu*Ro*(kPitoR/kPitoR + Pi) - mu*R
    a4 = Pi0*(kTOnMu/(kTOnMu + T)) + O-(delta + M)*Pi

    return np.array([a1, a2, a3, a4])


# Run the  fsolve with the initial values 

# initialize NOMI
NOMI = [1,0,0,0]

# provide a starting value for fsolve
y0 = [0.06,-0.027,0.025,10.55]
y01 = [2,2,2,2]
var_set = fsolve(non_linear_solution, y0, args = NOMI, maxfev = 10000);

print(var_set);




