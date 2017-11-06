#!/usr/bin/python

import numpy as np

def menor(M,column):

		n=len(M)
		Menor=np.empty((n-1,n-1))

		for i in range(0,n-1):
                	for j in range(column): 
                	        Menor[i,j]=M[i+1][j] 
				
        	for i in range(0,n-1):
                	for j in range(column,n-1):  
                	        Menor[i,j]=M[i+1,j+1]
				
        	return Menor

def determinant(M):

		if len(M)==1:
               		det=M[0,0]
        	elif len(M)==2:
                	det=M[0,0]*M[1,1]-M[0,1]*M[1,0]
        	else:
                	det=0
                	column=0
                	while column<len(M):
                        	Men=menor(M,column)
                        	det=det+np.power(-1,column)*M[0,column]*determinant(Men)
                        	column=column+1

        	return det


print("Choose the matrix's size: ")
n=input()
print("Chosen size is:  ")
print(n)
print("Random matrix of size n is: ")
M=np.random.random((n,n))
print(M)
determinante=np.linalg.det(M)
print("Determinant (NUMPY) is: ")
print(determinante)
det=determinant(M)
print("Calculated determinant is: " )
print(det)  

