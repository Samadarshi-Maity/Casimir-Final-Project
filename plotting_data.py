# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:11:07 2022

@author: Samadarshi_Maity
"""
import numpy as np
import matplotlib
matplotlib.style.use('classic')
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)


# read the populations data from the text file 

def reading_operations():
    
    f = open ( 'populations.txt' , 'r')
    l = []
    l = [ line.split() for line in f]
    print ("The file has been read")
    return l


### Beautifying stuff

fig = plt.figure(dpi=1600)

####### axis and tickmarks thickness ##########
ax = fig.add_axes([0,0,0.9,0.9])
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(2.5)

# For the major ticks
ax.xaxis.set_major_locator(MultipleLocator(50))
ax.xaxis.set_major_formatter('{x:.0f}')
ax.yaxis.set_major_locator(MultipleLocator(2))
#ax.yaxis.set_major_formatter('{x:.0f}')

# For the minor ticks
ax.xaxis.set_minor_locator(MultipleLocator(25))
ax.yaxis.set_minor_locator(MultipleLocator(1))

# tick width
#ax.xaxis.set_tick_params(width=2)
#ax.yaxis.set_tick_params(width=2)

ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4)# #color='r')

######### axis numbers font sizes ############
plt.xticks(fontsize=18, rotation=0)
plt.yticks(fontsize=18)


###### Data to plot ###########
