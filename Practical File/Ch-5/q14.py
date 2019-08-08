a=[91,4,3,89,45,7]
print("The minimum number is",min(a))
temp=a[0]
for i in range(1,len(a)):
    if a[i]<temp:
        temp=a[i]
print(temp,"is minimum")
