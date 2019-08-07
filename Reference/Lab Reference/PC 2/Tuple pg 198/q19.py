b=()
c=()
while True:
    a=int(input("what you want to add to the tuple"))
    
    if a==0:
        break
    
    b=b+(a,)
while True:
    a=int(input("what you want to add to the tuple"))
    
    if a==0:
        break
    
    c=c+(a,)

print(b)
print(c)

b,c=c,b

if b>c:
    print(b,"is greater")
else:
    print(c,"is greater")
