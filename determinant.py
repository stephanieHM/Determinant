#!/usr/bin/python

import numpy as np

def menor(M,row,column):
		n=len(M)
		Menor=np.empty((n-1,n-1))


		return Menor

def determinant(M):
		
		return det


print("Ingresa el tamano de la matriz")
n=input()
print("El tamano elegido es: ")
print(n)
print("La matriz aleatoria de tamano n es: ")
M=np.random.random((n,n))
print(M)
determinante=np.linalg.det(M)
print("El determinante, segun NUMPY, es: ")
print(determinante)
"""det=determinant(M)
print("El determinante es: " )
print(det)"""  

