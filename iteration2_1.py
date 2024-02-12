import numpy as np
import math
import matplotlib.pyplot as plt

u = 0       #INITIAL VELOCITY
velocity =[]    #EMPTY LIST TO STORE OUR VALUES FOR VELOCITY BEFORE ENTERING LOOP

while True:
    try:
        initial = u     #OUR VARIABLES
        r = 2.5  
        g = 9.8
        s = 2 * math.pi * r / 360

        theta_1 = math.pi / 180
        theta = math.pi / 180

        while theta < (48 * math.pi / 180):     #BEND 1
            a = g * float(math.sin(theta))  
            fr = -g * 0.4 * math.cos(theta)     #ADJUSTING FOR FRICTION
            if fr > 0:
                fr = -fr
            a = a + fr 
            v = float(math.sqrt(initial ** 2 + 2 * a * s))    #VELOCITY AFTER EACH WEDGE
            initial= float(v)       #USING FINAL AS INITIAL FOR NEXT WEDGE
            theta = float(theta + theta_1)      #CHANGING ANGLE AS CART GOES AROUND BEND

        while theta > 0.0174533:        #BEND 2
            a = g * float(math.sin(theta))     #ADJUSTING FOR FRICTION
            fr = -g * 0.4 * math.cos(theta)
            if fr > 0:
                a = -fr
            a = a+fr
            v = float(math.sqrt(initial ** 2 + 2 * a * s))      #VELOCITY AFTER EACH WEDGE
            initial = float(v)      #USING FINAL AS INITIAL FOR NEXT WEDGE
            theta = float(theta - theta_1)      #CHANGING ANGLE AS CART GOES AROUND BEND
            velocity.append(v)

        a = 9.8*math.sin(48 * math.pi / 180)-0.4*9.8*math.cos(48 * math.pi / 180)
        v = math.sqrt(initial ** 2 + 2 * a * 20)
        initial = v

        theta = math.pi / 180
        r = 7.4
        s = 2 * math.pi * r / 360

        while theta < 2 * math.pi:      #LOOP
            theta = float(theta)
            a =  - float((g * math.sin(theta)))   #ADJUSTING FOR FRICTION
            fr = -0.4 * g * math.cos(theta)
            if fr > 0:
                fr = -fr
            a = a + fr 
            v = float(math.sqrt(initial ** 2 + 2 * a * s))      #VELOCITY AFTER EACH WEDGE
            initial = v      #USING FINAL AS INITIAL FOR NEXT WEDGE
            theta = theta + theta_1      #CHANGING ANGLE AS CART GOES AROUND BEND

        #IF VELOCITY IS ENOUGH FOR TRAVELLING THROUGH LOOP, PROGRAM ENDS
        break

    except:
        #IF VELOCITY IS NOT ENOUGH FOR TRAVELLING THROUGH LOOP, PROGRAM WILL RUN AGAIN BY INCREASING VELOCITY BY 0.1 
        u += 0.1

print(u)
print(velocity[-1])    #PRINTS LAST VALUE FOR VELOCITY FROM THE LIST WHICH WORKED
print(v)