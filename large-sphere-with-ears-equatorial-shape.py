#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:56:53 2022

@author: admin
"""

import numpy as np
import math

ear_Xcoordinate = []
ear_Ycoordinate = []
ear_Zcoordinate = []



# ears for the sphere
for k in range(107,289):
   for i in range(-327,328):
       for j in range(-169,170,1):
          if i**2+j**2 + (abs(k-217))*(abs(k-217)) >=189*189:
             if (abs(i)-219)*(abs(i)-219)/(108*108)+j*j/(169*169) <= 1:
                    ear_Zcoordinate.append(float((k)*0.0001))
                    ear_Xcoordinate.append(float((i)*0.0001))
                    ear_Ycoordinate.append(float((j)*0.0001))
             else:
                  pass  
              
with open("big_ears-equatorial-shape.txt","w") as data_file:
#    data_file.write( for big ears
    for i in range(len(ear_Xcoordinate)):
        data_file.write("{},{},{}\n".format(ear_Xcoordinate[i], ear_Ycoordinate[i],ear_Zcoordinate[i])
            )