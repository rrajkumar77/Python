#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:47:09 2019

@author: admin
"""
import numpy as np

#1. Extract data from the given CSV file and store the data from each column in a
#separate NumPy array

arr = np.genfromtxt("Desktop/data/SalaryGender.csv", delimiter=',')

#2. Find:
#1. The number of men with a PhD
#2. The number of women with a PhD

import numpy as np
path_to_csv="Desktop/data/SalaryGender.csv"
arr = np.loadtxt(path_to_csv, dtype=np.object, delimiter=",", skiprows=1)
number_of_men_with_phd=0
number_of_women_with_phd=0
gender=0
phd=0

for i in range(len(arr)):
    gender = int(arr[i][1])
    phd = int(arr[i][3])
    if phd == 1 & gender == 1:
        number_of_men_with_phd = number_of_men_with_phd + phd
    else:
        number_of_women_with_phd = number_of_women_with_phd + phd

print ('The number of men with a PhD:',number_of_men_with_phd,'\nThe number of women with a PhD:',number_of_women_with_phd)

#3. Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD

import numpy as np
path_to_csv="Desktop/data/SalaryGender.csv"
A = np.loadtxt(path_to_csv, dtype=np.object, delimiter=",", skiprows=1)
print (A[:, [2, 3]][A[:, 3] == 1])

#4. Calculate the total number of people who have a PhD degree.

phd_count=0
phd=0

for i in range(len(arr)):
    phd = int(arr[i][3])
    if phd == 1:
        phd_count = phd_count + phd

print ('The total number of people who have a PhD degree are',phd_count)

#5. How do you Count The Number Of Times Each Value Appears In An Array Of Integers?
#[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
#Answer should be array([4, 2, 1, 1, 3, 2, 0, 0, 0, 1]) which means 0 comes 4 times, 1 comes 2 times, 2 comes 1 time, 3 comes 1 time and so on.

int_arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
unique, counts = np.unique(int_arr, return_counts=True)
print (dict(zip(unique, counts)))

# 6. Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements greater than 5.

num_arr = np.arange(:11,1)
range(0,50,2)])
adj_score = np.array([0,10,2,5,3])    
mat_xv = np.reshape(xVec,[5,2])

