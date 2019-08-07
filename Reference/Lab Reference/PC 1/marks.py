a=int(input("Enter your total marks"))
b=(a/500)*100

if b>= 90:
    print("Your Grade is A")
elif b>=69 and b<=90:
    print("B")
elif b>=50 and b<=69:
    print("C")
else:
    print(" D... failure")
