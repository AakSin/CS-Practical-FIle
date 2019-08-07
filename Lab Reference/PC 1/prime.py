a=int(input("enter number and we will check whether the no. is prime or not  "))
v=True
for i in range(2,a):
    if a%i==0:
        v=False
print(v)

