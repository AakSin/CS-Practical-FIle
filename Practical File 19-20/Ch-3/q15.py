a=int(input("enter the binary number"))
b=len(str(a))
c=0
for i in range(b):
    c+=(a%10)*(2**i)
    a//=10
print(c)
