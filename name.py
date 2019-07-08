for row in range(1,6):
    for col in range(1,5):
        if (row==1 and (col==2 or col==3)) or ((row==2 or row==4 or row==5) and (col==1 or col==4)) or (row==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

for row in range(1,6):
    for col in range(1,5):
        if (row==1 and (col==2 or col==3)) or ((row==2 or row==4 or row==5) and (col==1 or col==4)) or (row==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()


for row in range(1,6):
    for col in range(1,5):
        if ((row==1 or row==5) and (col==1 or col==4)) or ((row==2 or row==4 ) and (col==1 or col==3)) or ((row==3)and (col==1 or col==2)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

for row in range(1,6):
    for col in range(1,5):
        if (row==1 and (col==2 or col==3)) or ((row==2 or row==4 or row==5) and (col==1 or col==4)) or (row==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()


for row in range(1,6):
    for col in range(1,5):
        if (row==1 or row==3) or ((row==2 ) and (col==1 or col==4)) or ((row==3)and (col==1 or col==3)) or ((row==5)and (col==1 or col==4))or ((row==4)and (col==1 or col==3)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

for row in range(1,6):
    for col in range(1,5):
        if (row==1 or row==3) or ((row==2 ) and (col==1 or col==4)) or ((row==3)and (col==1 or col==3)) or ((row==5)and (col==1 or col==4))or ((row==4)and (col==1 or col==3)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

for row in range(1,6):
    for col in range(1,5):
        if (row==1 or row==3 or row==5) or ((row==2)and (col==1)) or ((row==4) and (col==4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

for row in range(1,6):
    for col in range(1,5):
        if ((row==1 or row==2 or row==4 or row==5)and (col==1 or col==4)) or (row==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
