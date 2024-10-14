# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:40:13 2022

@author: ctcri
"""

#This Program will calculate the integral of a given function
#Using Simpson's Rule:

#Imports
from numpy import sin, empty, pi, zeros

#Function
def function(x):
    ans = sin(x)
    return ans

#Parameters
a = 0                           #Start
b = 2 * pi                      #End
N = 100                         #Number of grid points
h = (b - a) / (N - 1)           #Size of step

y0 = 0                          #Initial y-value
x = zeros(N + 1, float)         #Create empty x-axis
f = zeros(N + 1, float)         #Create empty y-values

x[0] = 0                        #Set initial x
f[0] = y0                       #Set initial y 


for i in range(1, N):          
    x[i] = x[i-1] + h         #Populate x-axis
    f[i] = function(x[i])    #Populate y-axis

#Calculate the integral
integral = (h/3) * (f[0] + 4* sum(f[1:N-1:2]) + 2* sum(f[0:N:2] + f[N]))

#Print results
print("Simpson's Rule approximated the integral of sin(x) to be:")
print(integral)

