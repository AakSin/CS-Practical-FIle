s=0
n=int(input("Enter a no."))
x=int(input("Enter a value"))
for i in range(1,n+1):
    s=s+((x**((i-1))/i))

print(s)
