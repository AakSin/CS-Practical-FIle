lst1=eval(input("enter a list: "))

print("What do you want to do","Add=0","Modify=1","Delete=2","sort=3","display=4","exit=5",sep="\n")


  
while True:
    usr=int(input())
    if usr==0:
        d=input("enter what you want to add")
        lst1.append(d)
    if usr==1:
        d=input("enter what you want to add")
        n=int(input("where do you want to add"))
        lst1[n]=d
    if usr==2:
        n=int(input("where do you want to delete"))
        del lst1[n]
    if usr==3:
        lst1.sort()
    if usr==4:
        print(lst1)
    if usr==5:
        break


