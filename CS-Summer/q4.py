# 4. Write a Python program to count the number of even and odd numbers from a series of numbers. 
e=0
o=0
while True:
    a=input("enter a number or type end to stop ")
    if a=="end":
        break
    elif int(a)%2==0:
        e=e+1
    else:
        o=o+1

print(e,"even",o,"odd")
