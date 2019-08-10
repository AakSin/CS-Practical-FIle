t1=()
while True:
    a=float(input("Enter what you want to put in the tuple (Add floats only and use 0 to break"))
    if a==0.0:
        break
    t1+=(a,)
for i in t1:
    print(i)
print("maximum value is",max(t1),"and minimum value is",min(t1))
    
