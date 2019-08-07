s=eval(input("enter numbers"))

a=0
for i in s:
    if i%2!=0:
        a+=i
    else:
        continue
print(a)
