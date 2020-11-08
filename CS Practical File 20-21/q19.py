import csv
f=open("product.csv","w",newline='')
record=csv.writer(f,delimiter=',')
record.writerow(['PID','PNAME','COST','QUANTITY'])
while True:
    pid=input("Enter Product ID: ")
    pname=input("Enter Product Name: ")
    cost=int(input("Enter Cost of the Product: "))
    quantity=int(input("Enter Quantity: "))
    rec=[pid,pname,cost,quantity]
    record.writerow(rec)
    ch=input("You want to Enter more records:(y/n)")
    if (ch=='n' or ch=='N'):
        break
f.close()
