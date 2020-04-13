a=[4,5,6,4,1,3,4,56]
b=[a[-1]]

for i in range(0,len(a)-1):
    b.insert(i+1,a[i])
        

print(a)
print(b)
