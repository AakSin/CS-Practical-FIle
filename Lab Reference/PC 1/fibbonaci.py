a=int(input("enter a number"))
x=0
y=1
s=0
for i in range(0,a):
    s=x
    x=y
    y=y+s
    print(s)
    
    
