t1=()
t2=()
while True:
    a=input("Enter what you want to put in the tuple 1 (use 0 to break)")
    if a=="0":
        break
    t1+=(a,)
while True:
    a=input("Enter what you want to put in the tuple 2 (use 0 to break)")
    if a=="0":
        break
    t2+=(a,)
print(t1,"this is tuple 1")
print(t2,"this is tuple 2")
print("now we shall interchange their values")
t1,t2=t2,t1
if t1>t2:
    print("now tuple 1 is greater than tuple 2")
elif t1<t2:
    print("now tuple 2 is greater than tuple 1")
elif t1==t2:
    print("tuple 1 and 2 are equal")
else:
    print("Both of them have different data types")
