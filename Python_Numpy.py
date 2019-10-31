#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:24:23 2019

@author: admin
"""

# Numpy
# Creating Array from Existing Data

import numpy as np
x=[1,2,3]
a=np.asarray(x)
print(a)
print(a.ravel)

#Restructuring a Numpy Array
arr=np.zeros(8)
arr3d=arr.reshape((2,2,2))
print(arr3d)

#Indexing
arr=np.arange(2,20)
element=arr[6]
print(element)

#Slicing
arr_slice=slice(1,10,2)
print(arr[arr_slice])

#Numpy array attributes
print(a.shape)
print(a.ndim)
print(a.itemsize)

np.empty([3,2],dtype=int)

#Reading and writing
arr=np.loadtxt('file.txt)
np.savetxt('newfile.txt')

arr=genfromtxt('myfile.csv',delimiter=",")
np.savetxt('newfile.txt',arr,delimiter=",")

