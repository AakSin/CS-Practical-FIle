a=[4,5,6,4,1,3,4,56]
b=a

for i in range(0,len(a)):
    if i==len(a)-1:
        b[0]=a[i]
    else:
        b[i+1]=a[i]
print(a)
print(b)
