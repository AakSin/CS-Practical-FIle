
l=eval(input("Enter a list"))
print("what do u want to do","Add=0","modify=1","delete=2","sort=3","display=4","exit=5",sep="\n")
a=int(input())

while a!=5:
    if a==0:
        b=int(input("what do u want to add"))
        l.append(b)
        print(l)
    elif a==1:
        c=eval(input("what do u want to add"))
        d=int(input("where do u want to add"))
        l[d]=c
        print(l)
    elif a==2:
        e=int(input("what do u want to delete"))
        l.remove(e)
        print(l)
    elif a==3:
        print("in which order do u want to sort","ascending=1","descending=2",sep="\n")
        f=int(input())
        if f==1:
            l.sort()
            print(l)
        elif f==2:
            l.sort(reverse=True)
            print(l)
        else:
            print("you can't follow simple instructions huh!!")
    elif a==4:
        print(l)
    elif a==5:
        break
    
    else:
        print("you can't follow simple instructions huh!!")
    print("what do u want to do","Add=0","modify=1","delete=2","sort=3","display=4","exit=5",sep="\n")

    a=int(input())



        
    


    
