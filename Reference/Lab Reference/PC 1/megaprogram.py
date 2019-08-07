a=int(input("Enter a choice:"))

def sum(num1,num2):
    print("the sum is",num1+num2)
def area(num1):
    print("the area is",(22/7)*num1**2)
def per(num3,num4):
    print("the perimeter is",2*(num3+num4))       
def areasq(num1):
    print("the area is",num1**2)
          






if a==1:
    x=int(input("enter a no.:"))
    y=int(input("enter another no.:"))
    sum(x,y)
elif a==2:
    r=int(input("enter a radius"))
    area(r)
elif a==3:
    p=int(input("enter a length:"))
    q=int(input("enter a breadth:"))
    per(p,q)
elif a==4:
    s=int(input("Length of side:"))
    areasq(s)
else:
    print("your choice is invalid")
    
