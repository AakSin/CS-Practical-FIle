n=input("enter a string ")

if len(n)>=2:
    x=n[0:2]
    y=n[-2:]
    n=x+y
else:
    n=" "

print(n)    
