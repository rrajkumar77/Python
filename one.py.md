# Python
Python Project


def func():
    print("func() in one.py")
    
print ("top-level in one.py")

if __name=="__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
    
    
# output: top-level in one.py
# one.py is being run directly

