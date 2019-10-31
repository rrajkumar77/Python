#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:46:48 2019

@author: admin
"""

import numpy as np
x=[1,2,3]
a=np.asarray(x)
print(a)


#import necessary modules
import csv
with open("Desktop/data/SalaryGender.csv",'rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)
        for column in data:
            print (column)

        
        
####### Write Files ##############
arr =   np.arange(20)
print (arr)
np.savetxt('Test.txt',arr)

arr = np.loadtxt('file.txt')


arr1 = np.genfromtxt("Desktop/data/SalaryGender.csv", delimiter=',')

np.savetxt('newfile.csv', arr, delimiter = ",")
np.savetxt('Text.csv',arr,delimiter = ':')


import pandas as pd

airquality = pd.read_csv("Desktop/data/airquality.csv")
salary = pd.read_csv("Desktop/data/SalaryGender.csv")

