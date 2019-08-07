l=[10,20,30,40,50,60]

x=int(len(l)/2)
for i in range(x):
    l[i],l[x+i]=l[x+i],l[i]
print(l)

