print("lets find the greates of 4")
a = input("enter 1st no.")
b = input("enter 2nd no.")
c = input("enter 3rd no.")
d = input("enter 4th no.")

if   (a>b) & (a>c) & (a>d):
     print ("a is the greatest")
elif (b>c) & (b>d) & (b>a):
    print("b is the gereatest")
elif (c>d) & (c>b) & (c>a):
    print("3rd no. is the gereatest")
else:
    print("d is the gereatest")
