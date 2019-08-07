a=dict()
while True:
    n=input("Enter Name");
    if n=="0":
        break
    ib=input("enter items bought")
    cs=input("enter cost")
    pn=input("enter phone number")
    a[n]=(ib,cs,pn)
print(a)
