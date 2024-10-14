#######################################################################
#
#   Author:           Cameron Crites 
#   Creation Date:    ------  --, 2022 
#   Filename:         ----- 
#
#   Purpose:        
#      This program will do interesting things
#      and print out stuff.
#
#######################################################################

##########  IMPORTS  ##########
import numpy as np
import matplotlib.pyplot as plt

###

##########  FUNCTIONS  ########
def f(r, t):
	x = r[0]
	y = r[1]
	fx = y
	fy = gamma * (A**2 - x**2) * y - omega0**2 * x
	return np.array([fx, fy], float)



###
# Constants
A = 2.0
omega0 = 1.0
gamma = 0.05


#Periodic Conditions
T = 2*np.pi / omega0
n = 20

a = 0.0

h = T / 100

tvals = np.arange(a, T*n, h)		#Filled list of time values


xvals = []			#Empty list of x values
yvals = []			#Empty list of y values


r = np.array([-1.5, 0.0], float)

for t in tvals:
	xvals.append(r[0])
	yvals.append(r[1])
	
	k1 = h * f(r, t)
	k2 = h * f(r + 0.5*k1, t + 0.5*h)
	k3 = h * f(r + 0.5*k2, t + 0.5*h)
	k4 = h * f(r + k3, t + h)
	
	r += (k1 + 2*k2 + 2*k3 + k4) / 6.0

fig, ax = plt.subplots()
ax.plot(tvals, yvals)
plt.xlabel("t")
plt.ylabel("y")
plt.show()





