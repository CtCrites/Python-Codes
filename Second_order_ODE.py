#######################################################################
#
#   Author:           Cameron Crites 
#   Creation Date:    December  12, 2023 
#   Filename:         Second_order_ODE.py
#
#   Purpose:        
#      This program will solve and plot the Second Order ODE: 
#		 d**2x/dt**2 + 2*gamma* dx/dt + omega0**2 * x = 0 with desired
#		 number of periods.
#
#######################################################################

##########  IMPORTS  ##########
import numpy as np
from cmath import sqrt as csqrt
import matplotlib.pyplot as plt
###

##########  FUNCTIONS  ########
def f(t):					#Function to calculate x
	r1 = -gamma + csqrt(gamma**2 - omega0**2)
	r2 = -gamma - csqrt(gamma**2 - omega0**2)
	
	a = np.exp(r1 * t)
	b = np.exp(r2 * t)
	x = a + b
	return x.real
	
def df(t):					#Function to calculate dx
	r1 = -gamma + csqrt(gamma**2 - omega0**2)
	r2 = -gamma - csqrt(gamma**2 - omega0**2)
	
	a = r1 * np.exp(r1 * t)
	b = r2 * np.exp(r2 * t)
	x = a + b
	return x.real

###
### Parameters ###
m = 10						#Mass (kg)
c = 15						#Mass flow (kg/s)
k = 250						#Spring Constant (N/m)
n = 5							#Number of periods

N = 400						#Number of Data Points to Collect
dt = 0.04					#Stepsize between points

### Creation of zero arrays
x = np.zeros(N, float)	#x(t)
dx = np.zeros(N, float)	#dx(t)
t = np.zeros(N, float)	#t


### Calculations ###
gamma = c / (2 * m)		#Gamma = c/2m
omega0 = np.sqrt(k / m)	#omega0 = sqrt(k/m)

for i in range(N):		#Calculate x(t) and dx(t)
	t[i] = i * dt			#for N number of t values 
	x[i] = f(t[i])			#at step size dt
	dx[i] = df(t[i])

iter = 0						#Counter for number of dx(t) = 0
for i in range(1, len(dx)):
	if dx[i-1] / dx[i] < 0:	#Count if dx[i-1]/dx[i] is negative meaning 
		iter = iter + 1		#dx had crossed dx=0
		if iter == n*2:		#Check if number of periods has been met
			index = i
			break					#Break out of loop
x = x[0:index+1]				#Adjust x(t) for number of periods
t = t[0:index+1]				#Adjust t for number of periods

### Plot Results ###
fig, ax = plt.subplots()
ax.plot(t, x, label="x")
ax.legend()
plt.ylabel("x(t)")
plt.xlabel("t")
plt.show()











