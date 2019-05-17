# ()
  # passing input to functions
  # creating tuples

# []
  # Slicing/Extracting
  # Creating a list
# {}
  # Creating dictionary in {Key:Value} pair format
  # Creating set 

################ Basic/Atomic Data types in Python ##################

# int, float, str, bool, complex

##################### integer #################################
## any number without decimal points is treated as integer
a = 2
type(a)
b = -10
c = 123444444444444444444666666666666677777777777777 # no long int

################## float ###############################
# any number with decimal point is a float
d = 123.4556
type(d)

## float to integer and vice versa
b_f = float(b)
d_i = int(d) # nearest small integer
int(6.7)
round(6.4)
round(6.6)

############## String ##############################################
# anything with quotes is string
s = "nature"
type(s)
s1 = 'nature' # even single quotes is a string
s2 = "999" # even a number within quotes is a string
s3 = "n" # there is no character data type. even a single character is string

s2_i = int(s2) # string to integer
#int(s) throws error as nature cannopt be converted to an integer

#g = 05 throws error
g = "05"
int(g) # works.. 

5 + 10 # addition
"Hello" + "World" # concatenation

########### Boolean ################################################
h = True
type(h)
i = False
#j = true throws error as it is case sensitive

cond1 = 5 > 6
cond2 = 6 > 5
cond3 = 6 == 5 # equality check
cond4 = 6 != 5 # ineuality
cond5 = "nature" == "water"

cond1 and cond2 # logical AND
cond1 or cond2 # logical OR
not(cond1) # logical NOT

############## Complex ########################################
h = 5 + 10j
type(h)
h.real
h.imag
m = 5 - 10j
h*m

############## Tuple ######################################################
t1 = (5,6,1,4,9) # put values within ()
type(t1)
len(t1)

t2 = 5,6,1,4,9 # this will also create a tuple; not a common practice
t3 = ("nature","water","animals","birds")
t4 = (5,8.9,"nature",True,5+10j) # mix of data types are possible in a tuple

### TUPLE SLICING
t4[0] # indexing starts with 0 and ends with n-1
t4[3]
t4[len(t4)-1] # last
t4[-1]  # last value using negative indexing
t4[-2]
t4[1:4] # range of positions from 1 till 3; excludes the end position given
t4[:4] # beginning till 3
t4[2:] #2nd to last position

## Tuples are immutable. cannot be edited
#t4[1] = 100 throws error

##################### List ####################################################
l1 = [5,6,1,4,9] # created by giving within []
type(l1)
len(l1)
l3 = list(t3) # tuple can be converted to a list
l4 = [1,5.6,"Water",True] # supports mix of data types
t10 = tuple(l1) # convert list to a tuple

## LIST SLICING
l1[0]
l1[-1]
l1[2:4]

### LISTS ARE MUTABLE
l1[1] = 100 # replace value in a position
l1.append(20) # append a value to a list
l1.extend(l4) # extend a list by appending values in another list

l1.index(100) # returns index/position corresponding to a value
l1.index("Water")
l1.index(1) # only index corresponding to 1st occurence will be returned

del l1[3] # deleting based on position
l1.remove("Water") # deleting based on value
l1.remove(1) # only the 1st occurence is removed

l5 = [5,9,3,10,2,6]
l5.reverse() # reverse the order (mirror image)
l5.sort() # sort in ascending
l5.sort(reverse = True) # sort in descending
l3.sort() # even a list of string can be sorted in alphabetical order
#l1.sort() # throws error as mix of data types cannot be sorted

### LIST SEARCHING
# Search for value in a list and return True if it exists
"Water" in l4
5.6 in l4
10 in l4
10 not in l4

### LIST OF LIST
ll1 = [l3,l4]
ll1[0][2]

### LIST OF TUPLE
ll2 = [t1,t3]

#### NUMBER GENERATORS
l10 = list(range(100)) # 100 numbers from 0 till 99
l11 = list(range(1,101)) # 1 till 100
l12 = list(range(1,101,2)) # odd numbers from 1 till 100

rep1 = [5]*50
rep2 = [1,2,3]*10

# Q: Can I create repetition of tuples? Yes
rep3 = (1,2,3)*10

## LIST ASSIGNMENT 
#Create following lists
#a) [1,2,3,….,19,20]
a = list(range(1,21,1))

#b) [20,19,…,2,1]
b = list(range(20,0,-1))

#c) [1,2,3,….19,20,19,18,….,2,1]
c = list(range(1,21)) + list(range(19,0,-1)) # option 1
c = a + b[1:] # option 2
c = a[:-1] + b # option 3

#d) [4,6,3] and assign it to variable tmp
tmp = [4,6,3]

#e) [4,6,3,4,6,3,…..,4,6,3] where there are 10 occurences of [4,6,3]
e = tmp*10

#f) [4,6,3,4,6,3,….,4,6,3,4] where there 10 occurences of [4,6,3] followed by 4
# Option 1
f = tmp*10
f.append(4)

# Option 2
f = e + [4]

#g) [4,4,….,4,6,6,….,6,3,3,….,3] where there are 10 occurences of 4, 20 occurences of 6 and 30 occurences of 3
g = [4]*10 + [6]*20 + [3]*30

#Slice the following from list “f”
# 0th element
f[0]
# last but 3 till last element
f[-4:]
# downsample by 2 (skip alternative samples)
f[::2]

## LIST ADDITIONAL REFERENCE MATERIALS

##################### DICTIONARY ############################################
#{Key: Value}
math_score_list = [95,67,88,45,84]
math_score_list[2] # list supports only positional slicing

math_score_dict = {"Darbin": 95, 
                   "Nagalingam": 67, 
                   "Priya": 88, 
                   "Selva": 45, 
                   "Karthik": 84}
math_score_dict["Karthik"] # extract value using key
math_score_dict["Nagalingam"]
#math_score_dict[2] cannot slice using position

## KEYS HAVE TO BE UNIQUE; Duplicate will override the original
math_score_dict2 = {"Darbin": 95, 
                   "Nagalingam": 67, 
                   "Priya": 88, 
                   "Selva": 45, 
                   "Darbin": 90,
                   "Karthik": 84}

## INSERTING NEW KEY VALUE PAIR
math_score_dict["Bala"] = 79

## DICTIONARY PROPERTIES
math_score_dict.keys()
math_score_dict.values()

####### Values can be of any data type
some_dict1 = {"A": (1,2,3),
              "B": [[1,2,3],[4,5,6]],
              "C": {"AA":5,"BB":9}}

###### Keys should be of immutable data type
some_dict2 = {"A": 5, # string as a key
              4: "hello", # integer as a key
              (6,10): 95} # tuple as a key

#some_dict2 = {"A": 5, # string as a key
#              4: "hello", # integer as a key
#              [6,10]: 95} # list as a key will NOT work

##### Assignment
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York': 'NY',
    'Michigan':'MI'}

cities = {
    'CA':'San Fransico',
    'MI': 'Detroit',
    'NY':'Manhattan'}
# what is the name of the city in state "MI"
cities["MI"]

# Add a city 'Orlando' to 'FL'
cities["FL"] = "Orlando"

# what is the city name in 'New York' State
st1=states['New York']
cities[st1]
cities[states['New York']] # above 2 lines in 1 line

## DICTIONARY ADDITIONAL REFERENCE MATERIALS

################### Set ####################################################
# Typically used for set operations
# Values within {}

# set will contain only unique values
ss10 = {5,9,1,4,3,2,7,0,1,2,5,7,3,5,2}
print(ss10)
type(ss10)

seta = {1,2,3,4,5}
setb = {4,5,6,7,8,9,10}

seta & setb # intersection
seta | setb # union (pipe)
seta - setb # exclusive values in set a

#################### date time ###############################################
import datetime # importing functions in datetime package

### DATE
dd = datetime.date(2019,1,6)
type(dd)
print(dd)
dd.day
dd.month
dd.weekday() # Monday starts with a 0
dtod = datetime.date.today() # today's date in system
print(dtod)
dd.weekday()

### DATETIME
dtnow = datetime.datetime.now() # current system clock date and time
dtnow.year
dtnow.minute
dtnow.month

#https://docs.python.org/3/library/datetime.html

### STRPTIME (Custom format to a standard format)
dt1 = datetime.datetime.strptime("28/4/2019","%d/%m/%Y")
dt1.weekday()
datetime.datetime.strptime("28-4-2019","%d-%m-%Y")
datetime.datetime.strptime("28 April, 2019","%d %B, %Y")
datetime.datetime.strptime("28 Apr, 2019","%d %b, %Y")
datetime.datetime.strptime("28th April of 2019","%dth %B of %Y")

### STRFTIME (Standard format to custom format)
datetime.datetime.strftime(dd, "%d/%m/%Y")
datetime.datetime.strftime(dd, "%dth %B of %Y")
datetime.datetime.strftime(dd, "Week %U of Year %Y")

################### numpy #####################################################
### numpy comes pre-installed in anaconda installation
### anyone who uses only Python, then numpy has to be installed 

math_score_list = [95,67,88,45,84]
# What is the average score?
sum(math_score_list)/len(math_score_list)

# What is the median score?
math_score_list.sort()
math_score_list[int(len(math_score_list)/2)] # since the length is odd
# if the length is even, you have to take mid point of 2 centers

######### NUMPY INBUILT MATHEMATICAL FUNCTIONS
import numpy as np # importing numpy with an alias name np
np.mean(math_score_list)
np.median(math_score_list)
np.std(math_score_list)

########## NUMPY INBUILT NUMBER GENERATORS
ar1 = np.arange(1,101,2) # sequence of numbers
ar2 = np.random.rand(25) # random floating numbers
ar3 = np.random.randint(1,100,50) #  generates 50 integers between 1 and 100
ar4 = np.random.randint(1,100,50) # will be different than ar2 as this is random

## Some times, it might be needed to fix the randomness for resproducing the results
np.random.seed(1234) # fixing the random seed to something
np.random.rand(10)

np.random.seed(435) # fixing the random seed to something else
np.random.rand(10)

############## numpy array ###################################################
type(ar1)
type(ar2)
## all values in a numpy array should be of same data type
## if mix of data types is given, they will automatically get typecasted to 1 common data type

ar10 = np.array([1,False,5.6])
ar11 = np.array([1,False,5.6,"Hello"])

#### NUMPY ARRAY SLICING

## POSITIONAL SLICING
ar1[0]
ar1[6]
ar1[3:11] # position 3 till position 10
ar1[-5:] # last 5 positions

############ VECTORIZED OPERATION ######################################
## CONDITIONAL (BOOLEAN) SLICING
math_score_list = [95,67,88,45,84]
# extract only values greater than 70
95 > 70
67 > 70
#math_score_list > 70 throws error as a list cannot be compared in 1 go; needs a for loop

math_score_array = np.array(math_score_list) # converting list to an array
cond = math_score_array > 70 # do the condition check on all elements and return a boolean array
math_score_array[cond] # values corresponding to True positions are returned
math_score_array[math_score_array > 70] # above 2 lines in 1 line

math_score_array[math_score_array < 80] # values less than 80

## extract only odd numbers
math_score_array / 2 # dividing each element in array by 2 
math_score_array % 2 # dividing each element in array by 2 and gives the remainder
cond = math_score_array % 2 == 1
math_score_array[cond]
math_score_array[math_score_array % 2 == 1] # in 1 line
## Element wise process
math_score_array2 = math_score_array + 2 # element wise addition
adj_score = np.array([0,10,2,5,3])
math_score_array3 = math_score_array + adj_score # element wise addition of 2 arrays
# above line works because both arrays are of same length
np.array([1,2,3]) + np.array([10,11,12]) # works
#np.array([1,2,3]) + np.array([10,11,12,13]) # doesn't work as the lengths are different


########### ASSIGNMENT 1
math_score_array = np.array([95,67,88,45,84])
eng_score_array = np.array([78,67,45,39,67])
gender_array = np.array(["M","F","F","M","M"])

# extract maths score above average maths score
avg_maths_score = np.mean(math_score_array)
cond = math_score_array > avg_maths_score
math_score_array[cond]

# extract maths score of male students
cond = gender_array == "M"
math_score_array[cond]

# average maths score of male students
np.mean(math_score_array[cond])

# Extract maths score of male students who have scored above 70
# Option 1: Nested slicing
maths_male = math_score_array[gender_array == "M"]
maths_male[maths_male > 70]

# Option 2: Using and operator
cond1 = gender_array == "M"
cond2 = math_score_array > 70
math_score_array[cond1 & cond2]

# Extract maths score of students who are above average in english?
avg_eng_score = np.mean(eng_score_array)
cond = eng_score_array > avg_eng_score
math_score_array[cond]

# Average english score of male students who are above average in maths
cond1 = gender_array == "M"
cond2 = math_score_array > avg_maths_score
np.mean(eng_score_array[cond1 & cond2])

############# ASSIGNMENT 2 (OVER EMAIL)
#Create two numpy arrays with following values
xVec = np.array([42,85,84,23,11,55,14,96,13,30])
yVec = np.array([13,8,85,71, 1,7,55, 2,34,24])

#a. Slice xVec with values greater than 60
cond = xVec > 60
xVec[cond]

#b. Slice yVec with values less than mean of yVec
yvec_mean = np.mean(yVec)
cond = yVec < yvec_mean
yVec[cond]

#c. How many odd numbers in xVec?
xVec % 2 # element wise division by 2 and return the remainder
cond = xVec % 2 == 1
len(xVec[cond]) # option 1
sum(cond) # option 2: sum of a boolean array will return the count of Trues

#d. Slice values in yVec which are between minimum 
 # and maximum values of xVec (yes, xVec)
min(xVec)
max(xVec)
cond1 = yVec > min(xVec)
cond2 = yVec < max(xVec)
yVec[cond1 & cond2]

######################### numpy matrix #######################################
# There is no separate matrix data type
# numpy array can handle any dimensions

# matrix is a 2 dimensional array
## CREATING MATRIX BY RESHAPING A 1D ARRAY
xVec = np.array([42,85,84,23,11,55,14,96,13,30])
type(xVec) # numpy n dimensional array

mat_xv = np.reshape(xVec,[5,2])
mat2_xv = np.reshape(xVec,[2,5])
mat2_xvT = mat2_xv.T # Transpose

#mat3_xv = np.reshape(xVec,[3,4]) throws error as the lengths are mismatching

## CREATING MATRIX BY STACKING ARRAYS
score_mat1 = np.column_stack([math_score_array,eng_score_array]) # column wise stacking
score_mat2 = np.row_stack([math_score_array,eng_score_array]) # row wise stacking

## MATRIX SLICING
#m[row-pos,col_pos]
score_mat1[0,0]
score_mat1[2,1]
score_mat1[:,1] # all rows column 1
score_mat1[2,:] # row 2, all columns
score_mat1[1:4,:] # rows 1 till 3, all columns
score_mat1[[1,3,4],:] # rows 1,3,4; all columns

######################## pandas ###############################################
import pandas as pd

################## pandas Series #############################################
# 1 dimensional data type similar to numpy array
# Series consists of index which allows to slice using unique identifier
xarr = np.array([42,85,84,23])
type(xarr)
xser = pd.Series([42,85,84,23])
type(xser)

xser = pd.Series([42,85,84,23], index = ["a","b","c","d"])
xser[0] # slicing by position
xser["a"] # slicing by index

# Q: Can index be duplicated? Yes
xser2 = pd.Series([42,85,84,23], index = ["a","b","c","b"])
xser2["b"]

xser[0:2]

xser[xser > 50] # vectorized operation
xser.mean() # inbuilt pandas function
xser.median() # inbuilt pandas function
np.mean(xser) # numpy function on pandas series is possible

xser10 = xser/2 # element wise division

# Converting dictionary to a series
# Keys becomes index
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York': 'NY',
    'Michigan':'MI'}
states_ser = pd.Series(states)

################# Pandas Dataframe ########################################
# Most popular data type used in the Data science world
# Similar to a SQL table or an Excel table
# Each column can be of different data type
   # In case of matrix, all values should be of same data type
# Typically tabular data imported from files or databases are read as dataframe
   
### CREATING DATAFRAME FROM DICTIONARY OF LIST
dict1 = {"A": [1,2,3],
         "B": [3,4,5]}
df_dict1 = pd.DataFrame(dict1) # Each Key-Value pair becomes a column

dict11 = {"A": [1,2,3],
         "B": [3,4,5,6]}
#df_dict11 = pd.DataFrame(dict11) throws error 
# length of all lists should be equal

## CREATING DATAFRAME FROM DICTIONARY OF SERIES
# Matching happens through index. Mismatching ones get a null
dict2 = {"A": pd.Series([1,2,3], index = ["g","h","i"]),
         "B": pd.Series([3,4,5], index = ["g","h","i"])}
df_dict2 = pd.DataFrame(dict2)

dict22 = {"A": pd.Series([1,2,3], index = ["g","h","i"]),
         "B": pd.Series([3,4,5,6], index = ["g","h","i","j"])}
df_dict22 = pd.DataFrame(dict22)

dict23 = {"A": pd.Series([1,2,3], index = ["g","h","i"]),
         "B": pd.Series([3,4,5], index = ["h","j","i"])}
df_dict23 = pd.DataFrame(dict23)

"""
create a data frame df_emp_details with data of 3 employees
with unique names "Ram","Raj","Ravi" as index.
Create 2 columns Age and Income and assign any integer
"""
## From Dictionary of Series
emp_details_dict1 = {"Age": pd.Series([32,45,25], index = ["Ram","Raj","Ravi"]),
                     "Income": pd.Series([1000,4500,2500], index = ["Ram","Raj","Ravi"])}
df_emp_details = pd.DataFrame(emp_details_dict1)

## From Dictionary of List
emp_details_dict2 = {"Age": [32,45,25],
                     "Income": [1000,4500,2500]}
# adding index in 1 pass together
df_emp_details = pd.DataFrame(emp_details_dict2,
                              index = ["Ram","Raj","Ravi"])

## From numpy matrix
age = [32,45,25]
income = [1000,4500,2500]
emp_mat = np.column_stack([age,income])
df_emp_details = pd.DataFrame(emp_mat,
                              index = ["Ram","Raj","Ravi"],
                              columns = ["Age","Income"])

# Q: How to create dummy matrix with just index and columns
df_emp_empty = pd.DataFrame(index = ["Ram","Raj","Ravi"],
                              columns = ["Age","Income"])

# Q: Can I create dataframe from list of list? Yes
df_emp_details = pd.DataFrame([[32,1000],[45,4500],[25,2500]],
                              index = ["Ram","Raj","Ravi"],
                              columns = ["Age","Income"])

# Single column dataframe is not common. better saved as a Series or array
age_df = pd.DataFrame([32,45,25])

### DATAFRAME PROPERTIES
df_emp_details.shape # returns the number of rows and columns as a tuple
df_emp_details.shape[0] # number of rows
df_emp_details.shape[1] # number of columns
df_emp_details.columns # column names
df_emp_details.columns = ["Age1","Income1"] # Renaming all columns
#df_emp_details.columns = ["Age2"] throws error. it doesn't work this way to rename specific column
# Columns can be selectively renamed by feeding as a key-value pair
df_emp_details = df_emp_details.rename(columns = {"Age1":"Age2"})
df_emp_details.index # row index
df_emp_details.dtypes # data type of each column

## DATAFRAME SLICING

## SLICING COLUMN(S)
df_emp_details["Age2"]
ag = df_emp_details["Age2"] # when 1 column is extracted, it is saved as a series
type(ag) # each column in a dataframe is a series

df_emp_details[["Age2","Income1"]] # Slicing List of columns

#df_emp_details["Ram"] throws error as there is no column "Ram"

## LOC (Slicing by Index)
# df.loc[row_index,col_index]
df_emp_details.loc[:,"Age2"] # similar to df["Age2"]
df_emp_details.loc["Ram",:]
df_emp_details.loc["Ram","Income1"]
df_emp_details.loc[["Ram","Ravi"],"Income1"]
df_emp_details.loc[["Ram","Ravi"],:]

## ILOC (Slicing by Position)
# df.iloc[row_pos,col_pos]
df_emp_details.iloc[:,0]
df_emp_details.iloc[0,:]
df_emp_details.iloc[[0,2],:]
df_emp_details.iloc[1:3,:] # range of positions

## CONDITIONAL SLICING (.LOC)
# SQL: Select * from df_emp_details where Age2 > 30
cond = df_emp_details["Age2"] > 30
df_age_abv30 = df_emp_details[cond]
df_age_abv30 = df_emp_details.loc[cond,:]
# SQL: Select Income1 from df_emp_details where Age2 > 30
income_for_age_abv30 = df_emp_details.loc[cond,"Income1"]

df_age_below30 = df_emp_details.loc[~cond,:] # vectorized not operation using ~

## DATAFRAME SORTING
df_income_sorted = df_emp_details.sort_values("Income1")
df_income_sorted = df_emp_details.sort_values("Income1",
                                              ascending = False)

###########  Practice 
math_score_array = np.array([95,67,88,45,84])
eng_score_array = np.array([78,67,45,39,67])
gender_array = np.array(["M","M","F","M","F"])

# Create a data frame (score_df) with above 3 arrays as columns
# Add "R1001","R1002",...."R1005" as row indexes
# Add "Maths","English","Gender" as column indexes

score_dict = {"Maths": math_score_array,
              "English": eng_score_array,
              "Gender": gender_array}
score_df = pd.DataFrame(score_dict,
                        index = ["R1001","R1002","R1003","R1004","R1005"])
score_df = score_df[["Maths","English","Gender"]]
score_df.dtypes # String columns are saved as object

score_df_maths_sorted = score_df.sort_values("Maths",
                                             ascending = False)
# Note that index also moved along with data while sorting

## ASSIGNMENT 1
## DATAFRAME SLICING

# Slice the following
# Maths column
# Maths and English Column
# "Maths" column of "R1001"
# "Maths" and English column values of "R1001" and "R1003"
# All rows, 2nd column
# 0th and 3rd row, 0th and 1st column
# data frame of Male students alone
# english and maths score of Male students
# all columns of students who score above 70 in Maths
# average maths core of students who got above 60 in English
# average english score of students who are above average in maths
# all columns of male students who scores above 60 in maths
"""
slice english and gender column of either 
female students or students with maths score above 60
"""

## ASSIGNMENT 2 (sent over email)




## ASSIGNMENT 1 - Numpy pandas
## DATAFRAME SLICING

# Slice the following
# Maths column

import numpy as np
import pandas as pd

math_score_array = np.array([95,67,88,45,84])
eng_score_array = np.array([32,67,45,39,67])
gender_array = np.array(["M","M","F","M","F"])

math_column = math_score_array

# Maths and English Column
math_eng_column = {"Maths": math_score_array,
              "English": eng_score_array}


# "Maths" column of "R1001"


score_dict = {"Maths": math_score_array,
              "English": eng_score_array,
              "Gender": gender_array}

df_score = pd.DataFrame(score_dict,index = ["R1001","R1002","R1003","R1004","R1005"])


df_score.loc["R1001","Maths"]

# "Maths" and English column values of "R1001" and "R1003"

df_score.loc[["R1001","R1002"], ["Maths","English"]]


# All rows, 2nd column

df_score.loc[:,["English"]]

# 0th and 3rd row, 0th and 1st 
df_score.iloc[[0,3],[0,1]]


# data frame of Male students alone
cond = df_score["Gender"] == "M"
df_male = df_score[cond]

# english and maths score of Male students
cond1 = df_score["Gender"] == "M"
df_male_engmat = df_score.loc[cond1,["Maths","English"]]                      


# all columns of students who score above 70 in Maths

cond2 = df_score["Maths"]>70
all_70 = df_score[cond2]

# average maths score of students who got above 60 in English

cond3 = df_score["English"]>60
math = df_score.loc[cond3,["Maths"]]
np.mean(math)

# average english score of students who are above average in maths

math1 = df_score["Maths"]
cond4 = df_score["Maths"]>np.mean(math1)
engval = df_score.loc[cond4,["English"]]
np.mean(engval)


# all columns of male students who scores above 60 in maths
maths60 = df_score["Maths"]>60
male60 = df_score.loc[maths60 & cond]
           
"""
slice english and gender column of either 
female students or students with maths score above 60
"""
enggen = df_score.loc[maths60,["English","Gender"]]


# Assignment 2 Numpy pandas

# Creating Data frame 
#Option 1:
arr = np.random.randint(10,100,100)
r_arr = np.reshape(arr,[25,4])
df = pd.DataFrame({'A' : r_arr[:,0],'B':r_arr[:,1],'C' : r_arr[:,2],'D':r_arr[:,3]})
df.index +=1001

#Option 2:
df1 = pd.DataFrame(np.random.randint(10,100,size=(25, 4)), columns=list('ABCD'))
df1.index +=1001

#1. Slice column ‘A’ from df and save it as a series ‘s’
s =  df.iloc[:,0]
s1 = df.A
type(s)
type(s1)

sliA=df1.A
type(sliA)

#2. Slice column ‘A’ and column ‘C’ and save it as df2

df2 = df[['A','C']]
type(df2)

sliac=df1[['A','C']]

#tocheck
df.iloc["A","C"]

#3. Slice 0th and 2nd column using column number and save it as df3
df3 = df1.iloc[:,[0,2]]

#4. Slice from 0 till 5th position in series ‘s’
s[0:5] 

#5. Slice all columns from rows 3 till 19 and save it as df4
df4 = df1.iloc[3:19]

#6. Create df5 which has subset of data from df where column A values are above median of
#column A. Note: slice entire columns based on condition on column A

#Option 1
condA = np.median(df1.A)
condB = df1.A>condA
df5 = df1.A[condB]

#Option2
condC = df1.A > np.median(df1.A)
df7 = df1.A[condC]
