

def greater():
    if (a>b) & (a>c):
        return a
    elif(b>a) & (b>c):
       return b
    else:
        return c
a = int(input("enter 1st number "))
b = int(input("enter second number"))
c = int(input("enter third number"))

print ("the greatest number is :", greater ())