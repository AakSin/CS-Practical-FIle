s=[]
while True:
    a=int(input("enter number"))
    if a==0:
        break
    s.append(a)

s.sort()
print(s[0])
