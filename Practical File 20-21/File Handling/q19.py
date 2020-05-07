f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.readlines()
counter=0
for i in data:
    i=i.lower()
    if i.startswith("t"):
        counter+=1
print(counter)
f.close()