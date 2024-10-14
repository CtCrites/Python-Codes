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
def s(x, y, vx, vy, ax, ay, t):
	x = x + vx * t + 0.5 * ax * t**2
	y = y + vy * t + 0.5 * ay * t**2
	return x, y

def a(x, y):
	r = np.sqrt(x**2 + y**2)
	a = -G * M / r**2
	theta = np.arctan(y/x)
	ax = a * np.cos(theta)
	ay = a * np.sin(theta)
	return ax, ay
	
def v(vx, vy, ax, ay, t):
	vx = vx + ax * t
	vy = vy + ay * t
	return vx, vy

### Parameters ###
N = 8000					#Number of steps
dt = 1					#Time-step (hr)
dts = dt * 3600		#Time-step (s)

G = 6.67e-11			#Gravitational constant (Nm**2/kg**2)
M = 2e30					#Mass of large body (kg)
m = 6e20					#Mass of small body (kg)

x0 = 150e9				#Initial x position (m)
y0 = 0					#Initial y position (m)
vx0 = 0					#Initial x velocity (m/s)
vy0 = 30e3				#Initial y velocity (m/s)

### Creation of Lists ###
x = np.zeros(N, float)
y = np.zeros(N, float)
vx = np.zeros(N, float)
vy = np.zeros(N, float)
ax = np.zeros(N, float)
ay = np.zeros(N, float)
t = np.zeros(N, float)

### Store Initial Values ###
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0
ax[0], ay[0] = a(x0, y0)
t[0] = 0.0

### Loop for Number of Steps ###
for i in range(1, N):
	t[i] = i * dts
	x[i], y[i] = s(x[i-1], y[i-1], vx[i-1], vy[i-1], ax[i-1], ay[i-1], t[i])
	vx[i], vy[i] = v(vx[i-1], vy[i-1], ax[i-1], ay[i-1], t[i])
	ax[i], ay[i] = a(x[i], y[i])



### Plot Results ###
fig, ax = plt.subplots()
ax.plot(t, x, label="x")
ax.legend()
plt.ylabel("x(t)")
plt.xlabel("t")
plt.show()






