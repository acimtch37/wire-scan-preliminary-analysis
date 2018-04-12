# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:22:29 2018

@author: Alec Mitchell
"""

import matplotlib.pyplot as plt
import csv
import numpy as np


#with open('WM_1.csv','r') as csvfile:
#    datareader = csv.reader(csvfile, delimiter=',')
#    data = []
#    for row in datareader:
#        data.append(row)


my_data = np.loadtxt('WM_1.csv', delimiter=',', skiprows=6)

plt.pcolormesh(my_data,vmin=-5.5, vmax=-5.0)

print('Hello world')

#y1=375
#y2=430
#y3=.5*(y1+y2)

#I created a new branch.


