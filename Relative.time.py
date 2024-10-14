# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:05:24 2022

@author: ctcri
"""

##This Program is going to calculate the 
##time difference given relativity

#Imports
from numpy import sqrt
import os

#Constants
c = 3e8                         #Speed of Light (m/s)


#Describe the program
os.system("clear")
print("This program will show the relativistic nature of time between two observers.")
print("One observer will be stationary, and one will be in a frame moving away at a")
print("speed entered by you. See how much shorter the moving observer experiences time.")

#Inputs
v = float(input("\nEnter the speed of the moving frame (in m/s): "))
dt = float(input("Enter the time since the frame began to move (in seconds): "))

#Calculated Factors
beta = (v / c)                  #Beta factor (no unit)
gamma = 1 / (sqrt(1 - beta**2)) #Gamma factor (no unit)


#Calculation
dtt = dt / gamma

print("\nThe Proper Time is given as {} seconds".format(dt))
print("The Relative time is given as {} seconds".format(dtt))
print("The difference in time experienced is {:e} seconds".format(dt-dtt))
