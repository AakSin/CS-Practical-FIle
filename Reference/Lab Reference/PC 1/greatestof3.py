a=int(input("enter first no."))
b=int(input("enter second no."))
c=int(input("enter third no."))

if a>b>c:
    print(a,"is the greatest no.")
elif a>c>b:
    print(a,"is the greatest no.")
elif b>c>a:
    print(b,"is the greatest no.")
elif b>a>c:
    print(b,"is the greatest no.")
elif c>a>b:
     print(c,"is the greatest no.")
elif c>b>a:
     print(c,"is the greatest no.")
else:
    print("input invalid")
