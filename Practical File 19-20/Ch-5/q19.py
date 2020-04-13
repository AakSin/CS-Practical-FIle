a=[3,25,17,6,35,8,14,55]
for i in range(0,len(a)-1):
    if a[i+1]%5==0:
        a[i],a[i+1]=a[i+1],a[i]
print(a)
