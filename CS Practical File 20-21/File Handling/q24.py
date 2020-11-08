n=int(input("enter how many books you want to add: "))
with open("Practical File 20-21\\File Handling\\texts\\writing_sample1.txt","w") as f:
    for i in range(1,n+1):
        name=input(f"What is the name of book {i}? : ").title()
        price=input(f"What is the price of book {i} in rupees? : ")
        f.write(f"{name} is priced at {price} rupees\n")
