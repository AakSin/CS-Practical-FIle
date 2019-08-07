print("what operation would you like to perform today")
print("a - Addition")
print("b - Subtraction")
print("c - Multiplication")
print("d - Division")
print("e - Floor Division")
print("f- modulus")
usr=input()
a=float(input("enter first number"))
b=float(input("enter second number"))
if usr=="a":
    print(a+b)
elif usr=="b":
    print(a-b)
elif usr=="c":
    print(a*b)
elif usr=="d":
    print(a/b)
elif usr=="e":
    print(a//b)
elif usr=="f":
    print(a%b)

