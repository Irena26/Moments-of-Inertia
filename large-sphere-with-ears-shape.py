#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:12:09 2022

@author: admin
"""

import numpy as np
import math

ear_Xcoordinate = []
ear_Ycoordinate = []
ear_Zcoordinate = []

bolt_nut_Xcoordinate = []
bolt_nut_Ycoordinate = []
bolt_nut_Zcoordinate = []

water_Xcoordinate = []
water_Ycoordinate = []
water_Zcoordinate = []

sphere_Xcoordinate = []
sphere_Ycoordinate = []
sphere_Zcoordinate = []

z=0

# ears for the sphere
for k in range(58,397):
   for i in range(-327,328):
       for j in range(-90,91,1):
          if i**2+j**2 + (abs(k-217))*(abs(k-217)) >=189*189:
             if (abs(i)-219)*(abs(i)-219)/(108*108)+(k-227)*(k-227)/(169*169) <= 1:
                    ear_Zcoordinate.append(float((k)*0.0001))
                    ear_Xcoordinate.append(float((i)*0.0001))
                    ear_Ycoordinate.append(float((j)*0.0001))
             else:
                  pass  
              
with open("big_ears-shape.txt","w") as data_file:
#    data_file.write( for big ears
    for i in range(len(ear_Xcoordinate)):
        data_file.write("{},{},{}\n".format(ear_Xcoordinate[i], ear_Ycoordinate[i],ear_Zcoordinate[i])
            )

# bolts and nuts                  
for k in range(29):
       for i in range(-27,28,1):
           for j in range(-27,28,1):
               if i*i+j*j <=27*27:
                   if i*i+j*j >= 14*14:
                      bolt_nut_Zcoordinate.append(float((k)*0.0001))
                      bolt_nut_Xcoordinate.append(float((i)*0.0001))
                      bolt_nut_Ycoordinate.append(float((j)*0.0001))
               
for k in range(428,457):                
    for i in range(-27,28,1):
        for j in range(-27,28,1):
            if i*i+j*j <=27*27:
                bolt_nut_Zcoordinate.append(float((k)*0.0001))
                bolt_nut_Xcoordinate.append(float((i)*0.0001))
                bolt_nut_Ycoordinate.append(float((j)*0.0001))

for k in range(457,551):                
    for i in range(-14,15,1):
        for j in range(-14,15,1):
           if i*i+j*j <=14*14:
                bolt_nut_Zcoordinate.append(float((k)*0.0001))
                bolt_nut_Xcoordinate.append(float((i)*0.0001))
                bolt_nut_Ycoordinate.append(float((j)*0.0001))
                  
for k in range(551,581):                
    for i in range(-27,28,1):
       for j in range(-27,28,1):
           if i*i+j*j <=27*27:
                bolt_nut_Zcoordinate.append(float((k)*0.0001))
                bolt_nut_Xcoordinate.append(float((i)*0.0001))
                bolt_nut_Ycoordinate.append(float((j)*0.0001))
                                 
with open("bolt_nuts-shape.txt","w") as data_file:
#    data_file.write( for big ears
    for i in range(len(bolt_nut_Xcoordinate)):
        data_file.write("{},{},{}\n".format(bolt_nut_Xcoordinate[i], bolt_nut_Ycoordinate[i],bolt_nut_Zcoordinate[i]))
                 
# water sphere

for k in range(37,419,1):                
    for i in range(-180,181,1):
       for j in range(-180,181,1):
           if i*i+j*j+(k-37)*(k-37) <= 180*180:
                water_Zcoordinate.append(float((k)*0.0001))
                water_Xcoordinate.append(float((i)*0.0001))
                water_Ycoordinate.append(float((j)*0.0001))
 
       
with open("water-shape.txt","w") as data_file:
#    data_file.write("Frequency (Hz), Amplitude\n")
    for i in range(len(water_Xcoordinate)):
        data_file.write("{},{},{}\n".format(water_Xcoordinate[i], water_Ycoordinate[i],water_Zcoordinate[i])
            )
        
# plastic sphere shell
        
for k in range(28,428,1):                
    for i in range(-189,190,1):
       for j in range(-189,190,1):
           if i*i+j*j+(k-37)*(k-37) >= 180*180:
               if i*i+j*j+(k-37)*(k-37) <= 189*189:
                   sphere_Zcoordinate.append(float((k)*0.0001))
                   sphere_Xcoordinate.append(float((i)*0.0001))
                   sphere_Ycoordinate.append(float((j)*0.0001))
 
       
with open("sphere-shape.txt","w") as data_file:
#    data_file.write("Frequency (Hz), Amplitude\n")
    for i in range(len(sphere_Xcoordinate)):
        data_file.write("{},{},{}\n".format(sphere_Xcoordinate[i], sphere_Ycoordinate[i],sphere_Zcoordinate[i])
            )
        
        