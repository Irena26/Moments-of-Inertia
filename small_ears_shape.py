#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 00:06:23 2022

@author: admin
"""



import numpy as np
import math

ear_Xcoordinate = []
ear_Ycoordinate = []
ear_Zcoordinate = []



# ears for the sphere
for k in range(116,397):
   for i in range(-298,299):
       for j in range(-62,62,1):
          if i**2+j**2 + (abs(k-217))*(abs(k-217)) >=189*189:
             if (abs(i)-229)*(abs(i)-229)/(60*60)+(k-227)*(k-227)/(111*111) <= 1:
                    ear_Zcoordinate.append(float((k)*0.0001))
                    ear_Xcoordinate.append(float((i)*0.0001))
                    ear_Ycoordinate.append(float((j)*0.0001))
             else:
                  pass 
              
with open("small_ears-shape.txt","w") as data_file:
#    data_file.write( for big ears
    for i in range(len(ear_Xcoordinate)):
        data_file.write("{},{},{}\n".format(ear_Xcoordinate[i], ear_Ycoordinate[i],ear_Zcoordinate[i])
            )