import numpy as np
import matplotlib.pyplot as plt

#Define array
N = 100
P = np.linspace(0, 100, N)
A = np.linspace(0, 100, N)

#Define functions for max area and min perimeter
def P_min(A, b):
	return np.sqrt(2**(4 - b) * A)

def A_max(P, b):
	return P**2 * 2**(b-4)

#Initialize Figure 1 as Max Area
fig, ax = plt.subplots()
ax.plot(P, A_max(P, 0), 'k', linewidth=1, marker='+', label='No Border')
ax.plot(P, A_max(P, 1), 'b', linewidth=1, marker='+', label='One Border')
ax.plot(P, A_max(P, 2), 'r', linewidth=1, marker='+', label='Two Borders')

#Cutomize Figure 1 Apperence
ax.set_title('Max Area v. Perimeter', fontsize=20)
ax.set_xlabel('Perimeter (P)', fontsize=15)
ax.set_ylabel('Max Area (A)', fontsize=15)
plt.gca().tick_params(labelsize=10)
ax.grid(True, which='both')
ax.minorticks_on()
ax.legend()

#Initialize Figure 1 as Min Perimeter
fig2, ax2 = plt.subplots()
ax2.plot(A, P_min(A, 0), 'k', linewidth=1, marker='+', label='No Border')
ax2.plot(A, P_min(A, 1), 'b', linewidth=1, marker='+', label='One Border')
ax2.plot(A, P_min(A, 2), 'r', linewidth=1, marker='+', label='Two Borders')

#Customize Figure 2 Apperence
ax2.set_title('Mininum Perimeter v. Area', fontsize=20)
ax2.set_xlabel('Area (A)', fontsize=15)
ax2.set_ylabel('Minimum Perimeter (P)', fontsize=15)
plt.gca().tick_params(labelsize=10)
ax2.grid(True, which='both')
ax2.minorticks_on()
ax2.legend()

plt.show()
