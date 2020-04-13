print("do you want to find area using-")
print("Heron's formula - then press a and enter")
print("Height-base formula- then press b and enter")
usr=input()
if usr=="a":
        a=float(input("enter side 1"))
        b=float(input("enter side 2"))
        c=float(input("enter side 3"))
        s=(a+b+c)/2
        print("area is",(s*(s-a)*(s-b)*(s-c))**0.5)
elif usr=="b":
        a=float(input("enter height"))
        b=float(input("enter base"))
        print("area is",0.5*a*b)
else:
    print("wrong input")
