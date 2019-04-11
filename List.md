list = ["Marketing", "Content", "Designing", "Sales"]
print (list)
print (list + ["Python"])
print (list*2)
print ('Marketing' in list)
print (list [3])
print (list[0:2])

list[1] = "Java" #update List
list.append("Machine") #adds item to end of list
list.extend("Machine",'G', 'h') #inserts many items to the end of the list
list.insert(1,"Learn") # insert item at a given position
list.remove (3) # Remove item from list

#Delete element of List
del (list[2]) 

print(list.pop(3))
list.remove('Content')

# Return sorted list
print(sorted(list))

#Reverse the list
print(list [::-1])

print(len(list))


