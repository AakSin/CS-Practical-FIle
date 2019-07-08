s=input("enter a string ")
x=s.find("not")
y=s.find("bad")

if y>x:
    print(s.replace("not bad","good"))
