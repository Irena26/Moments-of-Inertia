#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 18:13:12 2022

@author: admin
"""

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



# ears for the sphere
for k in range(116,340):
   for i in range(-327,655):
       for j in range(-90,91,1):
          if i**2+j**2 >189*189:
             if (i-219)*(i-219)/(108*108)+(k-227)*(k-227)/(169*169) <= 1:
                 ear_Zcoordinate.append(float((k)*0.0001))
                 ear_Xcoordinate.append(float((i)*0.0001))
                 ear_Ycoordinate.append(float((j)*0.0001))
             else:
                  pass  
              
with open("medium_ears-shape.txt","w") as data_file:
#    data_file.write( for big ears
    for i in range(len(ear_Xcoordinate)):
        data_file.write("{},{},{}\n".format(ear_Xcoordinate[i], ear_Ycoordinate[i],ear_Zcoordinate[i])
            )


        