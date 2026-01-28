 
            
file = open("random.txt" )
content = file.read()

if  ("twinkle" in content):
    print("yes ")
else:
    print("no")

file.close()  



