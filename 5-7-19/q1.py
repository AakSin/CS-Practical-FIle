a=input("enter a string")
b=a.lower()
vow=0
uprc=0
alp=0
dig=0
vwlist=["a","e","i","o","u"]
for i in vwlist:
    c=b.count(i)
    vow=vow+c
for i in a:
    if i.isupper():
        uprc+=1
    if i.isalpha():
        alp+=1
    if i.isdigit():
        dig+=1

