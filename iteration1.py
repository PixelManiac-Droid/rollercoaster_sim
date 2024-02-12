import numpy as np      #IMPORTING LIBRARIES
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

r = 7.4     #SETTING VARIABLES
v = 18.9
g = 9.8

velocity = []   #CREATING EMPTY LISTS TO STORE VALUES
radius = []
gforce = []

while len(velocity) != 100:     #WHILE LOOP WHICH GENERATES V AND R VALUES 
    while len(radius) != 100:
        if r not in radius:
            radius.append(r)
        r = r + 0.1
    if v not in velocity:
        velocity.append(v)
    v = v + 0.2

gforce = [(v ** 2) / r / 9.8 for v in velocity for r in radius]     #CALCULATES G-FORCE
gforce_2d = np.array(gforce).reshape((len(velocity), len(radius)))      #CONVERTING GFORCE LIST TO ARRAY

fig, axs = plt.subplots(1, 2, figsize=(12, 6))      #SPLITTING OUR GRAPH INTO 2 SUBPLOTS

# Plot 2D contour
contour_2d = axs[0].contourf(radius, velocity, gforce_2d, cmap='viridis_r', levels=50)
axs[0].set(title='Contour Plot of G-force (2D)', xlabel='Radius', ylabel='Velocity')
colorbar_2d = fig.colorbar(contour_2d, ax=axs[0], label='G-force')
colorbar_2d.ax.axhline(y=4, color='blue', linestyle='-', linewidth=3)      #MARKING SAFE VALUES
colorbar_2d.ax.axhline(y=6, color='blue', linestyle='-', linewidth=3)
contour_lines = axs[0].contour(radius, velocity, gforce_2d, levels=[4, 6], colors='blue', linewidths=3)

# Plot 3D contour
axs[1] = fig.add_subplot(122, projection='3d')
contour_3d = axs[1].contourf(radius, velocity, gforce_2d, cmap='viridis_r', levels=50)
colorbar_3d = fig.colorbar(contour_3d, ax=axs[1], label='G-force')
axs[1].set(xlabel='Radius', ylabel='Velocity', zlabel='G-force', title='3D Contour Plot of G-force')
colorbar_3d.ax.axhline(y=4, color='blue', linestyle='-', linewidth=3)      #MARKING SAFE VALUES
colorbar_3d.ax.axhline(y=6, color='blue', linestyle='-', linewidth=3)
contour_lines2 = axs[1].contour(radius, velocity, gforce_2d, levels = [4,6], colors ='blue', linewidths=3)

plt.show()