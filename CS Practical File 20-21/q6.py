a=()
while True:
    k=int(input("enter a no. and enter 0 to break"))
    if k ==0:
        break
    a=a+(k,)
for i in a:
    print(i)
print("max value",max(a))
print("min value",min(a))
