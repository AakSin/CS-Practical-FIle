s=[]
while True:
    a=int(input("enter number"))
    s.append(a)
    if a==0:
        break
k=0
for i in s:
    if i%2!=0:
        k=k+i
print(k)
