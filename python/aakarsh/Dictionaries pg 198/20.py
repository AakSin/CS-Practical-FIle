a=dict()
while True:
    n=input("Enter class");
    if n=="0":
        break
    ct=input("enter class teacher")
    a[n]=ct
print(a)
x=input("enter name of class whose class teacher you want to know \n" )
print("class teacher of",x,"is", a.get(x))
    
