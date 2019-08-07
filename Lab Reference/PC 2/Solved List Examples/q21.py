a=["yello","dettol","niggol","celtos","kyoto","rhydon"]

x=int(len(a)/2)

for i in range(x):
    a[i],a[x+i]=a[x+i],a[i]

print(a)
