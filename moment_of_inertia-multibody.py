#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 00:11:21 2022

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('small_ears-equatorial-shape.txt', unpack=True, delimiter=',', dtype=float)

#x, y, z, x1, y1, z1 = data

coords1 = data1[:3]

density1 = 4057  #kg/m^3  density of big ears
ears_mass = 0.0253 # kg

x1,y1,z1 = coords1
point_mass1 = ears_mass/len(x1)


# move origin
x1_mean, y1_mean, z1_mean = np.mean(x1), np.mean(y1), np.mean(z1)
COM1 = np.array([x1_mean, y1_mean, z1_mean])

#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
#ax = fig.add_subplot()
#ax.scatter(x1,z1,y1)

#fig1 = plt.figure()
#ax = fig.add_subplot(projection='3d')
#ax1 = fig1.add_subplot()
#ax1.scatter(x1,y1,z1)

data2 = np.loadtxt('bolt_nuts-shape.txt', unpack=True, delimiter=',', dtype=float)

#x, y, z, x1, y1, z1 = data

coords2 = data2[:3]
x2,y2,z2 = coords2
x2_mean, y2_mean, z2_mean = np.mean(x2), np.mean(y2), np.mean(z2)
COM2 = np.array([x2_mean, y2_mean, z2_mean])

density2 = 8000  #kg/m^3  density of steel
bolt_nuts_mass = 0.0017 # kg, mass of one bolt and two nuts


point_mass2 = bolt_nuts_mass/len(x2)


data3 = np.loadtxt('water-shape.txt', unpack=True, delimiter=',', dtype=float)

#x, y, z, x1, y1, z1 = data

coords3 = data3[:3]
x3,y3,z3 = coords2
x3_mean, y3_mean, z3_mean = np.mean(x3), np.mean(y3), np.mean(z3)
COM3 = np.array([x3_mean, y3_mean, z3_mean])

density3 = 1000  #kg/m^3  density of water
r = 0.018 # m, radius of water inside the blue sphere
water_mass = density3*4/3*np.pi*r*r*r # kg, mass of the water inside the blue sphere


point_mass3 = water_mass/len(x3)


data4 = np.loadtxt('sphere-shape.txt', unpack=True, delimiter=',', dtype=float)

#x, y, z, x1, y1, z1 = data

coords4 = data4[:3]
x4,y4,z4 = coords4

x4_mean, y4_mean, z4_mean = np.mean(x4), np.mean(y4), np.mean(z4)
COM4 = np.array([x4_mean, y4_mean, z4_mean])

sphere_mass = 0.035 - 0.0017 - water_mass # kg, mass of the plastic hollow sphere


point_mass4 = sphere_mass/len(x4)

# move origin
z_mean = (ears_mass * z1_mean + bolt_nuts_mass * z2_mean + water_mass *z3_mean + sphere_mass * z4_mean)
COM = np.array([x1_mean, y1_mean, z_mean])

z1 = z1 - z_mean
z2 = z2 - z_mean
z3 = z3 - z_mean
z4 = z4 - z_mean

# move (0,0,0) to centre of mass (COM)
# coords = coords.T - COM

# move (0,0,0) to edge on z axis
#z1_max = np.max(z1)
#P_0 = np.array([x1_mean, y1_mean, z1_max])
#coords = coords.T - P_0
#coords = coords.T


#characteristic radius (for a sphere)
#R_0 = max(coords.ravel())

#R_0 for an object with length l along longest axis
#R_0 = l = 2 * max(coords.ravel())


#coords = coords/R_0

#x,y,z = coords

#x_mean, y_mean, z_mean = np.mean(x), np.mean(y), np.mean(z)
#COM = np.array([x_mean, y_mean, z_mean])

#coords = coords.T - COM
#coords = coords.T

#x,y,z = coords



#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
#ax.scatter(x1,y1,z1)

N1 = coords1.shape[1]
N2 = coords2.shape[1]
N3 = coords3.shape[1]
N4 = coords4.shape[1]

#print(N)
#print(len(x))
#I/mR^2
M = ears_mass + bolt_nuts_mass + water_mass + sphere_mass
Ix = (sum(coords1[1]**2 + coords1[2]**2)*point_mass1/N1+sum(coords2[1]**2 + 
    coords2[2]**2)*point_mass2/N2+sum(coords3[1]**2 + 
            coords3[2]**2)*point_mass3/N3+sum(coords4[1]**2 + coords4[2]**2)*point_mass4/N4)/M

Iy = (sum(coords1[0]**2 + coords1[2]**2)*point_mass1/N1+sum(coords2[0]**2 + 
    coords2[2]**2)*point_mass2/N2+sum(coords3[0]**2 + 
            coords3[2]**2)*point_mass3/N3+sum(coords4[0]**2 + coords4[2]**2)*point_mass4/N4)/M
                                      
Iz = (sum(coords1[0]**2 + coords1[1]**2)*point_mass1/N1+sum(coords2[0]**2 + 
    coords2[1]**2)*point_mass2/N2+sum(coords3[0]**2 + 
            coords3[1]**2)*point_mass3/N3+sum(coords4[0]**2 + coords4[1]**2)*point_mass4/N4)/M
                                      
Ixy = (sum(coords1[0]*coords1[1])*point_mass1/N1 + sum(coords2[0]*coords2[1])*
       point_mass2/N2 + sum(coords3[0]*coords3[1])*point_mass3/N3 + 
       sum(coords4[0]*coords4[1])*point_mass4/N4 )/M

Iyz = (sum(coords1[1]*coords1[2])*point_mass1/N1 + sum(coords2[1]*coords2[2])*
       point_mass2/N2 + sum(coords3[1]*coords3[2])*point_mass3/N3 + 
       sum(coords4[1]*coords4[2])*point_mass4/N4 )/M

Ixz = (sum(coords1[0]*coords1[2])*point_mass1/N1 + sum(coords2[0]*coords2[2])*
       point_mass2/N2 + sum(coords3[0]*coords3[2])*point_mass3/N3 + 
       sum(coords4[0]*coords4[2])*point_mass4/N4 )/M


#M =  0.011#mass of the object(kg)


I_MR2 = np.array([[Ix, Ixy, Ixz],[Ixy, Iy, Iyz],[Ixz, Iyz, Iz]])
print(I_MR2)

#Moment of inertia (kg/m^2)
#I = I_MR2 * M
