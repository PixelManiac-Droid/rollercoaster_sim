import math     #IMPORTING MATH AND GRAPHING LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

r = 7.4    #ASSIGNING VALUES TO ALL OUR VARIABLES
u = 15.2
g = 9.8
s = 2 * math.pi * r / 360
theta = math.pi / 180
theta_1 = math.pi / 180

gforce = []     #CREATING EMPTY LISTS TO STORE ALL OUR VALUES AS THEY'RE GENERATED 
velocity = []
radius = []
gforce1 = []

while len(velocity) != 100:     #RUNS THE WHILE LOOP UNTIL VELOCITY LIST HAS 100 VALUES
    while len(radius) != 100:   #RUNS THE WHILE LOOP UNTIL RADIUS LIST HAS 100 VALUES
        while theta < 2 * math.pi: #RUNS THE WHILE LOOP UNTIL ROLLERCOASTER LOOP IS COMPLETE
            theta = float(theta)
            a = g*math.sin(theta)   #CALCULATING DECELERATION DUE TO FRICTION
            fr = -0.4*g*math.cos(theta)
            if fr > 0:
                fr = -fr
            a = a+fr
            v = float(math.sqrt(u ** 2 + 2 * fr * s))    #FINAL VELOCITY AFTER EACH WEDGE
            ac = v ** 2 / r     #FINDING CENTRIPETAL ACCELERATION
            gf = float(ac / 9.8)    #CONVERTING CENTRIPETAL ACCELERATION TO G-FORCE
            gforce.append(gf)   #ADDING G-FORCE TO LIST
            theta = theta + theta_1 #CHANGES THE ANGLE VALUE AS CART GOES AROUND THE LOOP

        if r not in radius:
            radius.append(r)
        r = r + 0.1     #CHANGING RADIUS AFTER EACH LOOP

    if u not in velocity:
        velocity.append(u)
    u = u + 0.2     #CHANGING VELOCITY AFTER EACH LOOP

gforce1 = [(v ** 2) / r / 9.8 for v in velocity for r in radius]
gforce_2d = np.array(gforce1).reshape((len(velocity), len(radius)))     #CONVERTS G-FORCE LIST INTO AN ARRAY SO WE CAN PLOT

#CREATING SUBPLOTS
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

#PLOT 2D CONTOUR
contour_2d = axs[0].contourf(radius, velocity, gforce_2d, cmap='viridis_r', levels=50)    #PLOTTING THE GRAPH
axs[0].set_title('Contour Plot of G-force (2D)')    #SETS LABELS FOR AXES
axs[0].set_xlabel('Radius')
axs[0].set_ylabel('Velocity')
colorbar_2d = fig.colorbar(contour_2d, ax=axs[0], label='G-force')
colorbar_2d.ax.axhline(y=4, color='blue', linestyle='-', linewidth=3)  #MARKS THE SAFE VALUES
colorbar_2d.ax.axhline(y=6, color='blue', linestyle='-', linewidth=3)  #MARKS THE SAFE VALUES
contour_lines = axs[0].contour(radius, velocity, gforce_2d, levels=[4, 6], colors='blue', linewidths=3)    

#PLOT 3D CONTOUR
axs[1] = fig.add_subplot(122, projection='3d')      
contour_3d = axs[1].contourf(radius, velocity, gforce_2d, cmap='viridis_r', levels=50)    #PLOTTING THE GRAPH
colorbar_3d = fig.colorbar(contour_3d, ax=axs[1], label='G-force')
axs[1].set_xlabel('Radius')     #SETS LABELS FOR AXES
axs[1].set_ylabel('Velocity')
axs[1].set_zlabel('G-force')
axs[1].set_title('3D Contour Plot of G-force')
contour_lines2 = axs[1].contour(radius, velocity, gforce_2d, levels = [4,6], colors ='blue', linewidths=3) #MARKS SAFE VALUES
colorbar_3d.ax.axhline(y=4, color='blue', linestyle='-', linewidth=3)  #MARKS THE SAFE VALUES
colorbar_3d.ax.axhline(y=6, color='blue', linestyle='-', linewidth=3)  #MARKS THE SAFE VALUES

plt.tight_layout()
plt.show()