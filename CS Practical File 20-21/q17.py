ctr1=0
ctr2=0
ctr3=0
f=open("text.txt","r")
txt=f.read()
for i in txt:
    if i.isalnum()==True:
        if i.isdigit()==True:
            ctr1+=1
    else:
        if i.isspace()==True:
            ctr2+=1
        else:
            ctr3+=1
print("numbers:",ctr1)
print("spaces:",ctr2)
print("symbols:",ctr3)
