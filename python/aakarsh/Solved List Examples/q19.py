L=[12,3,5,6,7,9]
for i in range(len(L)):
    if L[i]%2==0:
        L[i]+=10
    else:
        L[i]+=5
print(L)
