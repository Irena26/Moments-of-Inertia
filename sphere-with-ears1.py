#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 16:25:24 2022

@author: admin
"""

import numpy as np
import math

Xcoordinate = []
Ycoordinate = []
Zcoordinate = []

z=0

for k in range(409):
   if k < 161:
       for i in range(-45,46,1):
           for j in range(-45,46,1):
              if i**2+j**2 < 45*45:
                  if abs(j) >= abs(abs(i)-33):
                      Zcoordinate.append(float((k)*0.0001))
                      Xcoordinate.append(float((i)*0.0001))
                      Ycoordinate.append(float((j)*0.0001))
              else:
                  pass        
                  
   elif   k < 221:
       for i in range(-45,46,1):
           for j in range(-45,46,1):
              if i**2+j**2 < 45*45:
                  if abs(j) >= abs(abs(i)-33):
                      Zcoordinate.append(float((k)*0.0001))
                      Xcoordinate.append(float((i)*0.0001))
                      Ycoordinate.append(float((j)*0.0001))
                  elif abs(j) <= 7.5:
                      Zcoordinate.append(float((k)*0.0001))
                      Xcoordinate.append(float((i)*0.0001))
                      Ycoordinate.append(float((j)*0.0001))
              else:
                  pass
                 
   else:
       a=np.sqrt(abs(0.0109*(38000-1*(2*(k-310))**2.)))
       b=190/4.1*0.000001*np.exp(0.000299*(225-k))*((k-221)**2+1)
       for j in range(-7,7,1):
          for i in range(-190,191,1):
#              print(i)
#              temp = math.sqrt(abs(1.8-0.7*(0.1*(k-221))**1.5))
#              print (temp)
              
              
              if (k-358)*(k-358)+(abs(i)-112)*(abs(i)-112) < 39*29:
                  
                  pass
                
              elif abs(i) <= abs(40+((5.9*(np.sin(0.01*(k-221)+0.2))**4.4+4)*a*b)):
                  Zcoordinate.append(float((k)*0.0001))
                  Xcoordinate.append(float((i)*0.0001))
                  Ycoordinate.append(float((j)*0.0001)) 
       

with open("key-shape.txt","w") as data_file:
#    data_file.write("Frequency (Hz), Amplitude\n")
    for i in range(len(Xcoordinate)):
        data_file.write("{},{},{}\n".format(Xcoordinate[i], Ycoordinate[i],Zcoordinate[i])
            )
        