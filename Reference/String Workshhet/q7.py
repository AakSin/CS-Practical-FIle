z=0
while True:
    a=input("enter a string")
    if a[0]==a[-1] and len(a)>1:
        z=z+1
    if a=="0":
        break

print(z)
