a=input("enter a string ")
b=input("enter a string ")

c=len(a)
d=len(b)
e,f,g,h="","","",""
if c%2==0:
    e=a[0:int(c/2)]
    f=a[int(c/2):]
else:
    e=a[0:int(c/2)+1]
    f=a[int(c/2)+1:]


if d%2==0:
    g=b[0:int(d/2)]
    h=b[int(d/2):]
else:
    g=b[0:int(d/2)+1]
    h=b[int(d/2)+1:]


print(e+g+f+h)
