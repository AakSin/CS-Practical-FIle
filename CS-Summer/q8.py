# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010
def binint(num):
    z=0
    for i in range(0,len(str(num))):
        a=num%10
        num=num//10
        z=z+a*(2**(i))
    return z

n=input("enter binary string").split(",")
z=""
for i in n:
    if binint(int(i))%5==0:
        z=z+" "+i
print(z)
