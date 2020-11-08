import pickle
n=int(input("enter no. of items"))
i=1
while i<=n:
    f=open("Items.dat","ab")
    l=[]
    item_code=int(input(f"enter item {i} code:"))
    l.append(item_code)
    item_name=input(f"enter item {i} name:")
    l.append(item_name)
    item_price=int(input(f"enter price of item {i}:"))
    l.append(item_price)
    item_quantity=int(input(f"enter item quantity {i}:"))
    l.append(item_quantity)
    i+=1
    pickle.dump(l,f)
    f.close()
