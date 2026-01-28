print("lots of passwords??")
print("give me some i'll store them for you ")

def view():
    with open ('password.txt' , 'r') as f:
        for line in f.readlines():
            print (line)
            
            

def add():  
    n = int(input ("how many "))
    for i in range(n):
        name = input ("enter you name or username--> ")
        pswd = input ("enter ypur password and i will store it !-->")
        
        with open ('password.txt', 'a') as f:
                f.write(name + '\\\\'+ pswd +"\n" )
    
    

while True:  
    mode = input ("what would you like to do?? view password , add passwords or quit?").lower()
    if (mode == 'quit' ):
        break

    if (mode == 'add'):
        add()

    elif(mode == 'view'):
        view()

    else:
        continue
   
   
