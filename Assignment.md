# Python
Python Test 



Reference_ID = input ("Enter Social ID:" )

password = Reference_ID

flag = 0
while True:   
    if (len(password)<12): 
        flag = -1
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        break
    elif re.search("\s", password): 
        flag = -1
        break
    else: 
        flag = 0
        print("Valid Reference ID") 
        break
  
if flag ==-1: 
    print("Not a Valid Reference ID") 


string = password

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)
