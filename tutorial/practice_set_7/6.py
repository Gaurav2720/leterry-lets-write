print("lets print factorial of a number")


n = int(input("enter a nuber-->"))
fact = 1
for i in range (1,n+1):
    fact= fact*i
print(f"factorial of {n} is {fact}")   