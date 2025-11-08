# Mustafa Anjrini on 24.10.2025

import os
import numpy as np
# please change the directory below accordingly
os.chdir("C:/Users/anjrini/Projekte")
import determinanti # import the method which is a litte faster
import determinanti_2 # import the method that a homgenous structure but a little slower

#let's do an example of the array a below
a=np.array([[-1,2,9.1,6,-2,1,-2,1],[2,42.4,6,-7,3.7,2,1,1],[3,7,9,62,-2,1,1,-1],[-3,5,-7,-29,-3,-1,-1,2],[4,4,5,9,-1,22,2,1],[1,-1,21,-1,1,-1,1,-1],[-1,1,-11,1,-1,1,-1,1],[1,1,1,-1,-1,-1,-1,1]])     

# calculating the determinant using the first method (a little faster than the second method)
determinanti.determinanti(a)

#calculating the determinant using the second method
determinanti_2.determinanti_2(a)

