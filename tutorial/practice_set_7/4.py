print("checking fot ptimr no..")

n = int (input("enter any number ")) 
for i in range (2,n):
    if (n%i==0):
        print (f"{n}is not prime")
        break
else:
    print(f"{n} is prime")
    
