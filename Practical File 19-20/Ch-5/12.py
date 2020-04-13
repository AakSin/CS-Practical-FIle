a=list(range(2,31,3))
b=0
for i in a:
    if i%2!=0:
        b+=i
print("sum of all odd elements is",b)
