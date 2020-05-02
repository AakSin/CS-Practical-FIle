f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.read()
data=data.lower()
data=data.split()
counter=0
for i in data:
    if i[0]=="a":
        counter+=1
print(counter)