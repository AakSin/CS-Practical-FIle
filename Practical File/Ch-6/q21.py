a=dict()
while True:
    n=input("Enter Student");
    if n=="0":
        break
    ct=input("enter percentage")
    a[n]=ct
print(a)

x=input("which student do you want to delete\n")
del a [x]
print(a)
