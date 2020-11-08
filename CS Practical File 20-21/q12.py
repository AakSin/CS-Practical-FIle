def roots(a,b,c):
    det= b**2 - 4*a*c
    if det >0:
        root1= ((-b + ((det)**(1/2)))/(2*a))
        root2= ((-b - ((det)**(1/2)))/(2*a))
        print(a,"x^2+",b,"x+",c,"has real but unequal roots:",root1,"and",root2)
    if det ==0:
        root3= (-b/(2*a))
        print(a,"x^2+",b,"x+",c,"has equal roots:",root3, sep="")
    if det <0:
        print(a,"x^2+",b,"x+",c,"doesnt have any real roots.")
print("Quadratic Equation: Ax^2 + Bx+ C")
A = int(input("Enter the coefficient A:"))
B = int(input("Enter the coefficient B:"))
C = int(input("Enter the coefficient C:"))
roots(A,B,C)
