def deleteChar(a,b):
    c=''
    for i in a:
        if i==b:
            continue
        else:
            c+=i
    print(c)
a= input("Enter a statement")
b= input("enter the character to be deleted")
deleteChar(a,b)
