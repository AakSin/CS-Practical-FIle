import pickle
print("1 - Accept the data from user")
print("2 - Display all records stored in binary file")
print("3 - Search binary file on the basis of Item Code")
print("4 - Update the Item Name, Item Price and Item Quantity in binary file on the basis of Item Code")
print("5 - Delete a record on the basis of Item Code")
print("6 - Exit to Quit the program")
    

while True:
    n=int(input("Enter which option you would like: "))
    if n==1:
        with open("Practical File 20-21\\Data Handling\\q1.dat","ab") as f:
            while True:     
                code=input("Enter Item Code: ")
                name=input("Enter Item Name: ")
                price=int(input("Enter Item Price(integer): "))
                quantity=int(input("Enter Item Quantity(integer): "))
                wri_rec=[code,name,price,quantity]
                pickle.dump(wri_rec,f)    
                ch=input("Enter more record(y/n):")
                if (ch=="n" or ch=="N"):
                    break
    if n==2:
        with open("Practical File 20-21\\Data Handling\\q1.dat","rb") as f:
            try:    
                while True:  
                    read_rec=pickle.load(f)  
                    print(read_rec)
            except EOFError:        
                print("all files read")
    if n==3:
        with open("Practical File 20-21\\Data Handling\\q1.dat","rb") as f: 
            rec_search=input("Enter the item code to be searched:")
            try:    
                while True:     
                    read_rec=pickle.load(f)  
                    if (read_rec[0]==rec_search):  
                        print("Record found")
                        print(read_rec)
                        break
            except EOFError:
                print("Record not found")
    if n==4:
         with open("Practical File 20-21\\Data Handling\\q1.dat","rb") as f: 
            rec_search=input("Enter the item code to be searched:")
            f1=open("Practical File 20-21\\Data Handling\\q2.dat","wb")
            try:    
                while True:     
                    read_rec=pickle.load(f)  
                    if (read_rec[0]==rec_search):  
                        print("item found")
                        read_rec[1]=input("enter item name ")
                        read_rec[2]=int(input("enter item price "))
                        read_rec[3]=int(input("enter item quantity "))
                    pickle.dump(read_rec,f1)
            except EOFError:
                print("if no prompt appeared then the record was not found")
            f1.close()
            with open("Practical File 20-21\\Data Handling\\q2.dat","rb") as f:
                with open("Practical File 20-21\\Data Handling\\q1.dat", "wb") as f1:
                    for line in f:
                        f1.write(line)
    if n==5:
        with open("Practical File 20-21\\Data Handling\\q1.dat","rb") as f: 
            rec_search=input("Enter the item code to be searched:")
            f1=open("Practical File 20-21\\Data Handling\\q2.dat","wb")
            try:    
                while True:    
                    read_rec=pickle.load(f)  
                    if (read_rec[0]==rec_search):   
                        print("Record found, deleting this record")
                        continue
                    pickle.dump(read_rec,f1)
            except EOFError:
                print("if no prompt appeared then the record was not found")
            f1.close()
            with open("Practical File 20-21\\Data Handling\\q2.dat","rb") as f:
                with open("Practical File 20-21\\Data Handling\\q1.dat", "wb") as f1:
                    for line in f:
                        f1.write(line)
    if n==6:
        break