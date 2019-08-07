a=input("enter binary no.")
l= len(a)
x=int(a)
s=0

for i in range(0,l,1):
    n=x%10
    x=x//10
    n=(2**i)*n
    s=s+n

print(s)
