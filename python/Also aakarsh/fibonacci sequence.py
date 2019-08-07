n=int(input("enter a no."))
a=0
b=1
i=0
while i<=n:
    s=a
    a=b
    b=b+s
    print(s)
    i+=1
