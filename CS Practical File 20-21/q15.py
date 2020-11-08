ctr1=0
ctr2=0
f=open("text.txt","r")
txt=f.read()
for i in txt:
    ctr1+=1
    if i==" ":
        ctr2+=1
print("Total no. of charcters (except spaces):",ctr1-ctr2)
