"""
Created on Tues Jan 31 15:14:06 2022

@author: Milan
"""
import Dynamic_equations as dyneq
import scipy.integrate as spint
import scipy.optimize as spopti
import numpy as np

def findSteadyState(variables0):
    ''' Finds the steady state where all derivatives are equal to zero'''
    spopti.minimize(dyneq.rates,variables0)
    return steadyState_eq_matrix