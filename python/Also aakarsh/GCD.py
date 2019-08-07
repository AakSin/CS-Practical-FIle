x=int(input("enter a no."))
y=int(input("enter 2nd no."))
if x>y:
    for i in range(x,0,-1):
        if x%i==0 and y%i==0:
           print(i)
           break           
else:
    for i in range(y,0,-1):
        if x%i==0 and y%i==0:
           print(i)
           break
           
