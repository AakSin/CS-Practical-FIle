n=input("enter a string ")
x=n[1:]
y=n[0]
z=y
for i in x:
    if i==y:
        z=z+"*"
    else:
        z=z+i
print(z)
