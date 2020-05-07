import pickle
print("1 - Accept the data from user")
print("2 - Display all records stored in binary file")
print("3 - Search binary file on the basis of Item Code")
print("4 - Update the Item Name, Item Price and Item Quantity in binary file on the basis of Item Code")
print("5 - Delete a record on the basis of Item Code")
print("6 - Exit to Quit the program")
    

while True:
    n=int(input())
    if n==1:
        with open("q2.dat","ab") as f:
            while True:     # input values from user
                rollno=int(input("Enter Roll Number:"))
                name=input("Enter Name:")
                clas=int(input("Enter Class:"))
                section=input("Enter Section:")
                wri_rec=[rollno,name,clas,section]
                pickle.dump(wri_rec,f)    #writing data to binary file
                ch=input("Enter more record(y/n):")
                if (ch=="n" or ch=="N"):
                    break
    if n==2:
        with open("q1.dat","rb") as f:
            try:    #Exception Handling for EOFError
                while True:  # read records from binary file
                    read_rec=pickle.load(f)  #loading data from binary file
                    print(read_rec)
            except EOFError:        
                print("all files read")
    if n==3:
        with open("q1.dat","rb") as f: #open binary file in read binary mode
            rec_search=int(input("Enter the roll no to be searched:"))
            try:    #Exception Handling for EOFError
                while True:     # read records from binary file
                    read_rec=pickle.load(f)  #loading data from binary file
                    if (read_rec[0]==rec_search):   #compare rollno in file
                        print("Record found")
                        print(read_rec)
                        break
            except EOFError:
                print("Record not found")
    if n==4:
        f=open("q1.dat","rb+") #open binary file in read/write binary mode
        rec_search=int(input("Enter the roll no to be updated:"))
        rec_no=-1
        try:    #Exception Handling for EOFError
            while True and rec_found==0:     # read records from binary file
                read_rec=pickle.load(f)  #loading data from binary file
                rec_no+=1
                if (read_rec[0]==rec_search):   #compare rollno in file
                    f.seek(rec_no)
                    read_rec[1]=input("Enter the New Name to be updated:")
                    pickle.dump(read_rec,f)
                    print("Record updated")
                    print(read_rec)
                    break
                else:
                    position=f.tell()
        except EOFError:
            print("Record not found")
        f.close()   #close binary file
    if n==6:
        break