#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:25:21 2022

@author: sergey
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('key-shape.txt', unpack=True, delimiter=',', dtype=float)

#x, y, z, x1, y1, z1 = data

coords = data[:3]

x,y,z = coords


# move origin
x_mean, y_mean, z_mean = np.mean(x), np.mean(y), np.mean(z)
COM = np.array([x_mean, y_mean, z_mean])

fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
ax = fig.add_subplot()
ax.scatter(x,z,y)

fig1 = plt.figure()
#ax = fig.add_subplot(projection='3d')
ax1 = fig1.add_subplot()
ax1.scatter(x,y,z)

# move (0,0,0) to centre of mass (COM)
# coords = coords.T - COM

# move (0,0,0) to edge on z axis
z_max = np.max(z)
P_0 = np.array([x_mean, y_mean, z_max])
coords = coords.T - P_0
coords = coords.T


#characteristic radius (for a sphere)
#R_0 = max(coords.ravel())

#R_0 for an object with length l along longest axis
R_0 = l = 2 * max(coords.ravel())


#coords = coords/R_0

x,y,z = coords

#x_mean, y_mean, z_mean = np.mean(x), np.mean(y), np.mean(z)
COM = np.array([x_mean, y_mean, z_mean])

#coords = coords.T - COM
#coords = coords.T

#x,y,z = coords



#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
#ax.scatter(x1,y1,z1)

N = coords.shape[1]
print(N)
print(len(x))
#I/mR^2
Ix = sum(coords[1]**2 + coords[2]**2)/N
Iy = sum(coords[0]**2 + coords[2]**2)/N
Iz = sum(coords[0]**2 + coords[1]**2)/N
Ixy = sum(coords[0]*coords[1])/N
Iyz = sum(coords[1]*coords[2])/N
Ixz = sum(coords[0]*coords[2])/N


M =  0.011#mass of the object(kg)


I_MR2 = np.array([[Ix, Ixy, Ixz],[Ixy, Iy, Iyz],[Ixz, Iyz, Iz]])
print(I_MR2)

#Moment of inertia (kg/m^2)
I = I_MR2 * M
