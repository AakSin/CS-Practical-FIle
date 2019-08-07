s=[]
while True:
    a=int(input("enter number"))
    if a==0:
        break
    s.append(a)
k=0
for i in s:
    k=k+i
        
print(k,"is sum")
print(k/len(s),"% is percentage")

