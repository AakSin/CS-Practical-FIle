s=[]
while True:
    a=int(input("enter number"))
    if a==0:
        break
    s.append(a)
    
k=0
for i in s:
    k+=i
print(k/len(s))
