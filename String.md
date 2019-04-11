str='edureka' 
print(str.capitalize()) 
print(str.count("e",0,len(str))) 
print(str.count("ka",0,len(str))) 
 
 
s = str.encode('utf-8','strict') 
print (s) 



#converting tuple to list
tuple1=(1,2,3,4,'a','b')
print(tuple1)
lst=list(tuple1)
print(lst)
lst[1]= 'Python'
