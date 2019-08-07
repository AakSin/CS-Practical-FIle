#first 100 fibonacci numbers
a=0
b=1
print(a)
for i in range(100):
    print(b) 
    a,b=b,a
    b=b+a