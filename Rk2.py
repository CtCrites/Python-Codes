# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:25:09 2022

@author: ctcri
"""
from math import sin
from numpy import empty
import matplotlib.pyplot as plt

###############################################

def f(x, y):
    return - y**3 - sin(x)

###############################################

#Parameters
a = 0.0
b = 10.0
N = 8

#Step Size
h = (b - a)/N

#initial Condition

y0 = 0.0


#Define arrays x and y
x = empty(N+1, float)
y = empty(N+1, float)

#Main Calculation
x[0] = a
y[0] = y0
for i in range(N):
    x[i + 1] = x[i] + h
    k1 = h * f(x[i], y[i])      #k1 is the prediction by the Euler Method 
    k2 = h * f(x[i] + 0.5*h, y[i] +0.5*k1)  #Apply Euler at midpoint of interval
    y[i + 1] = y[i] + k2

#Plot the solution
fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

