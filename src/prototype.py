# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:22:29 2018

@author: Alec Mitchell
"""

import matplotlib.pyplot as plt
import csv
import numpy as np

print('hello')


#with open('WM_1.csv','r') as csvfile:
#    datareader = csv.reader(csvfile, delimiter=',')
#    data = []
#    for row in datareader:
#        data.append(row)


my_data = np.loadtxt('WM_1.csv', delimiter=',', skiprows=6)

plt.figure(1)
plt.pcolormesh(my_data,vmin=-5.5, vmax=-5)
plt.grid()
#plt.show(block=False)
plt.pause(0.1)

#locate edges of row
#y1=300
#y2=440
y1 = int(input("Enter y_bot value"))
y2 = int(input("Enter y_top value"))
y3=int(.5*(y1+y2))

xprof = np.linspace(0,16, len(my_data[y3]))
yprof = my_data[y3]
yprofdif = np.gradient(yprof)

plt.figure(2)
plt.ylim(-5.6,-5.25)
plt.grid()
plt.plot(xprof, yprofdif)
#plt.show(block=False)
plt.pause(0.1)

mean = np.mean(yprof)
stdev = np.std(yprof)

#basic filter for outliers. if y(x)' >> 0, replace y at x with average of points surrounding 
#for i in range(0,len(yprofdif)):
#    if abs(yprofdif[i]) >= 5:
#        yprof[i] = .5*(yprof[i+10]+yprof[i-10])
for i in range(0, len(yprof)):
    if abs(yprof[i]-mean) >= 3*stdev:
        yprof[i] = np.median(yprof)

#filtered profile
plt.figure(3)
plt.ylim(-5.6, -5.25)
plt.grid()
plt.plot(xprof, yprof)
#plt.show(block=False)
plt.pause(0.1)

#section filtered profile
#x_l = 3
#x_r = 9
x_l = float(input("Enter x_left value"))
x_r = float(input("Enter x_right value"))
plt.figure(4)
plt.xlim(x_l, x_r)
plt.grid()
plt.plot(xprof, yprof)

plt.figure(5)
plt.xlim(x_l, x_r)
plt.grid()
plt.plot(xprof, np.gradient(yprof))
