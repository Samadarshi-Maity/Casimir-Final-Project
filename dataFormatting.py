import numpy as np
import math

def variables_out_to_tauTRPi(variables):
    '''Extract the four variables T,tau,R,Pi out of the matrix t x 4'''

    T=variables[:,0]
    tau=variables[:,1]
    R=variables[:,2]
    Pi=variables[:,3]

    return T,tau,R,Pi
    
def rawDataToTextFile(t,T,tau,R,Pi):
    pass
    #matrixToPrint=np.concatenate((t,T,tau,R,Pi),axis=1) Doesnt work!
    #print('Saving raw data')
    #np.savetxt('populations.txt',matrixToPrint, fmt = '%.2e')
    #a_file = open("populations.txt", "w")

