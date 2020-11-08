print()
emp=[]
c="y"
while (c=="y"):
    print ("1. PUSH")
    print ("2. POP ")
    print ("3. Display")
    choice=int(input("Enter your choice: "))
    if (choice==1):
        eid=int(input("Enter employee number :"))
        ename=input("Enter employee name :")
        e=(eid,ename)
        emp.append(e)
    elif (choice==2):
        if (emp==[]):
            print ("Stack Empty")
        else:
            print ("Deleted element is : ",emp.pop())
    elif (choice==3):
        l=len(emp)
        for i in range(l-1,-1,-1):
            print (emp[i])
    else:
        print("Wrong Input")
    c=input("Do you want to continue or not? ")
