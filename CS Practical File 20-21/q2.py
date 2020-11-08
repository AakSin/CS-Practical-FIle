while True:
    s=0
    p= input("Do you want to enter a number? Y/N")
    if p in "Yy":
        a = input("Enter a number")
        for i in a:
            if i in "0123456789":
                s+=int(i)
        print("the total sum of digits: ",s)
    else:
        break
