import numpy as np
import random as rd

n = 2
pas = 0.001
iteration = 10000
nbrsimulation=n
M=np.zeros((n,n))
for i in range(n):
            for j in range(i+1):
                if i!=j:
                    c = rd.randint(0,9)
                    M[i,j] = c
                    M[j,i] = c
H=np.zeros(n)
for i in range(n):
    H[i]=rd.randint(0,1)
 
