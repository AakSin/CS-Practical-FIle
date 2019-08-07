a=int(input("enter the number"))
b=len(str(a))
c=0
for i in range(b):
    c+=(a%10)
    a//=10
print(c)
