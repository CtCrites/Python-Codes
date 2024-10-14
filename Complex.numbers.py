# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:05:57 2022

@author: ctcri
"""

##"Complex.numbers"
#This program will perform a few computations on 
#complex numbers

#Imports
from math import atan, sqrt

################################# FUNCTIONS ###################################
def csqrt(x):                           #Finds the Sqrt of a negative number
    x = float(x)   
    re = sqrt(abs(x))
    return re   
    
def phase(x, y):                        #Finds the phase of a complex number
    rat = (y / x)
    theta = atan(rat)
    return theta
    
def modulus(x, y):                      #Finds the modulus of a complex number
    rad = x**2 + y**2
    r = sqrt(rad)
    return r

def quo(real1, comp1, real2, comp2):    #Finds the quotient of 2 Complex Numbers
    rea = real2/real1
    com = comp2/comp1
    return rea, com
def pro(real1, comp1, real2, comp2):    #Finds the product of 2 Complex Numbers
    realp = real1 * real2
    compp = comp1 * comp2
    return realp, compp
###############################################################################

#Program Description
print("This program will perform some calculations with Complex Numbers,")
print("without the use of complex functions. Calculations for Complex Numbers,")
print("are completed by functions written by Cameron Crites\n")


#Part 1:
print("\nPart 1:")
neg = input("Enter a negative number: ")
c = 0
d = csqrt(neg)
print("\nThe Square Root of {} is: {:.3f}i". format(neg, d))
print("Take C = {:.3f} + ({:.3f})i".format(c, d))

#Part 2:
#Gather inputs
print("\nPart 2:")
a = input("Please enter the Real component of the Complex Number: ")
b = input("Please enter the Complex component of the Complex Number: ")

#Convert to floats
a = float(a)
b = float(b)
c = float(c)
d = float(d)

#Print Z
print("\nTake Z = {:.3f} + ({:.3f})i".format(a, b))

#Calculations
print("The phase of Z is: {:.3f}".format(abs(phase(a, b))))
print("The Modulus of Z is {:.3f}".format(modulus(a, b)))


#Part 3:
print("\nPart 3:")
#Calulations
realq, compq = quo(a, b, c, d)
realp, compp = pro(a, b, c, d)

#Outputs
print("The complex quotient C/Z = {:.3f} + ({:.3f})i".format(realq, compq))
print("The complex product C*Z = {:.3f} + ({:.3f})i".format(realp, compp))
input("Press 'Enter' to Escape: ")

