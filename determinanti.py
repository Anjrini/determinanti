# Mustafa Anjrini on 24.10.2025

import numpy as np
import math

def determinanti(a):
    #calculating the determinant of a 2*2 matrix
    def dett(x):
        return x[0,0]*x[1,1]-x[1,0]*x[0,1]

    #calculating the determinant of a 3*3 matrix
    def cubic_det(y):
        v3=0
        for k in range(3):
            v1=(-1)**k*y[0,k]
            v2=np.concat((np.arange(k),np.arange(k+1,y.shape[1])))
            v3+=v1*dett(y[1:,v2])
        return(v3)
    
    #converting a to numpy array
    a=np.array(a)

    #checking if the dimensions of the matrix are equal and then calculating the determinant
    if a.shape[0]!=a.shape[1]:
        return ('error because the two dimensions of the matrix are not equal')
    elif a.shape[0]==2:
        return dett(a)
    elif a.shape[0]==3:
        return cubic_det(a)
    else:
        #calculating the determinant of a n*n matrix

        #constructing a matrix "h" for the indices which we are going to loop over
        #the number of rows is -3 because of our calculation of a 3*3 matrix
        rows=a.shape[0]-3
        #the number of columns is a factorial number of the dimension but we are going to
        #devide by the factorial of 3 because we have already computed the determinant for a 3*3 matrix
        columns=int(math.factorial(a.shape[0])/math.factorial(3))

        #constructing the h matrix
        h=np.zeros((rows,columns))

        #filling the last row of the h matrix with the running number 0,1,2,3 as we are getting
        #at the last a 4*4 matrix to deal with 
        h[h.shape[0]-1,:]=np.tile(np.arange(4),int(h.shape[1]/4))

        #filling the rows of the h matrix except for the last row as we have calculated in the step before
        #we are relying on numpy functions to construct the indices of the submatrices
        for i in range(5,a.shape[0]+1):
            h[a.shape[0]-i,:]=np.tile(np.repeat(np.arange(i),(math.factorial(i-1)/math.factorial(3))),int(h.shape[1]/(math.factorial(i)/math.factorial(3))))

        #r here is the value of determinant that will be calculated after running over the loops
        #using the h indices -> submatrices
        r=0
        for i in range(h.shape[1]): 
            #d is the top row of each matrix and submatrix to be multiplied at the end with
            #the determinant of each submatrix r
            d=(-1)**int(h[0,i])*a[0,int(h[0,i])]
            #removing the first row as we have got the d value from
            a_=a[1:,:]
            for j in range(h.shape[0]): 
                #constructing the submatrix using the indices of h and by removing one column each time in a row
                col=int(h[j,i])
                row=np.shape(a_)[1]
                idx=np.concat((np.arange(col),np.arange(col+1,row)))
                a_=a_[:,idx]
                if j<h.shape[0]-1:
                    #getting the d from the submatrices
                    d_idx=int(h[j+1,i])
                    d=d*(-1)**d_idx*a_[0,d_idx] #just for testing
                if j==h.shape[0]-1:   
                    #summing over the determinant of every submatrices and of course after multiplying
                    #it with the corresponding d values from previous submatrices                
                    r+=d*cubic_det(a_)
                a_=a_[1:,:]
        return(r)

