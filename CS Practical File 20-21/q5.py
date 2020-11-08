n=True
lst=[1,2,3,4,5]
while n==True:
    a=int(input("Enter what element to insert: "))
    b=int(input("Enter what position you want to enter: "))
    lst[b]=a
    print(lst)
    c=input("Do you want to add more? yes/no ")
    if c in ["yes","Yes","YES","Y"]:
        n=True
    else:
        n=False
