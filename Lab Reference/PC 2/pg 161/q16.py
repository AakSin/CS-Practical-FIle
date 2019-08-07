s=[]
while True:
    a=int(input("enter number"))
    if a==0:
        break
    s.append(a)

    
for i in range(len(s)):
    if i%2!=0:
        s[i]=s[i]*2

print(s)
