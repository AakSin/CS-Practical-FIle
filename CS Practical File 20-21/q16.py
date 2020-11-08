ctr1=0
ctr2=0
f=open("text.txt","r")
txt=f.read()
for i in txt:
    if i.isupper()==True:
        ctr1+=1
    if i.islower()==True:
        ctr2+=1
print("upper characters:",ctr1)
print("lower characters:",ctr2)
