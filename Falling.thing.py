#######################################################################
#
#   Author:           Cameron Crites 
#   Creation Date:    Sept 11, 2022 
#   Filename:         Falling.thing.py 
#
#   Purpose:        
#      Calculates the position, velocity, and acceleration of a falling
#      tennis ball.
#
#######################################################################



##########  IMPORTS  ##########
import numpy as np
import matplotlib.pyplot as plt
import os
import time 
###

##########  FUNCTIONS  ########
def f(v):
	if k==0:
		return 0
	elif k==1:
		return (-c1 * v)
	elif k==2:
		return (-c2 * v**2)
###

# Timing 
N = 1500					#Total number of steps
tau = 0.01				#Size of timestep

# Environmental Constants
g = 9.81					#Acceleration due to gravity
eta = 1.81e-5			#Viscosity of air (kg/m/s)
rho = 1.2				#Density of air (kg/m^3)
Cd = 0.47				#Drag coefficient for sphere


#Print Program Description
print("This program will compute the displacement, velocity, and acceleration")
print("of a spherical object in free fall. Input parameters for results...")
time.sleep(5)
os.system("clear")

#Prompt for Object Parameters
m = float(input("Enter the mass of the object in kilograms: "))
radius = float(input("Enter the radius of the object in meters: "))

#Prompt for Air Resistance
print("\nChoose a method of calculating air resitance:")
print("1. No Air Resistance\n2. Linear Resistance\n3. Quadratic Resistance")
k = int(input("Method: "))

#Prompt for things to plot
print("\nEnter the numbers of the things you to plot\nNo spaces are needed for more than 1 choice:")
print("1. Displacement\n2. Velocity\n3. Acceleration")
P = input("Plot choice: ")
time.sleep(2)
os.system("clear")


A = np.pi*(radius**2)	#Cross secional area of object
c1 = 6*np.pi*eta*radius
c2 = 0.5*rho*Cd*A


#Define arrays
t = np.zeros(N+1, float)
x = np.zeros(N+1, float)
v = np.zeros(N+1, float)
a = np.zeros(N+1, float)

#Set initial values
t[0] = 0.0
x[0] = 0.0
v[0] = 0.0
a[0] = g - f(v[0])/m

#Populate arrays
for i in range(N):
	t[i+1] = t[i] + tau
	x[i+1] = x[i] + v[i]*tau + 0.5*a[i]*(tau**2)
	v[i+1] = v[i] + a[i]*tau
	a[i+1] = g + f(v[i+1])/m
	if np.round(a[i+1], 3) == 0:
		tt = t[i+1]
		xt = x[i+1]
		vt = v[i+1]
		at = a[i+1]
		

#Display final Kinematic Values
print("As the object reaches terminal velocity\nThe following values were recorded")
print("Time of flight (s): {:.4f}".format(t[i+1]))
print("Distance Fallen (m): {:.4f}".format(x[i+1]))
print("Velocity (m/s): {:.4f}".format(v[i+1]))
print("Acceleration (m/s^2): {:.4f}".format(a[i+1]))

#Create Plot
fig, ax = plt.subplots()
if "0" in P:
	pass
elif "1" in P and "2" in P and "3" in P:
	ax.plot(t, x, label="Displacement")
	ax.plot(t, v, label="Velocity")
	ax.plot(t, a, label="Acceleration")
	ax.legend()
	plt.show()
	
elif "1" in P and "2" in P:
	ax.plot(t, x, label="Displacement")
	ax.plot(t, v, label="Velocity")
	ax.legend()
	plt.show()
	
elif "1" in P and "3" in P:
	ax.plot(t, x, label="Displacement")
	ax.plot(t, a, label="Acceleration")
	ax.legend()
	plt.show()
	
elif "2" in P and "3" in P:
	ax.plot(t, v, label="Velocity")
	ax.plot(t, a, label="Acceleration")
	ax.legend()
	plt.show()
	
elif "1" in P:
	ax.plot(t, x, label="Displacement")
	ax.legend()
	plt.show()
	
elif "2" in P:
	ax.plot(t, v, label="Velocity")
	ax.legend()
	plt.show()
	
elif "3" in P:
	ax.plot(t, a, label="Acceleration")
	ax.legend()
	plt.show()
	
		




#Last Update Sept 
