f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.read()
data=data[:-1] #remove fullstop in the end
data=data.replace(", "," ") #remove fullstop from the end of words
data=data.replace(". "," ") #remove comma from the end of words
data=data.lower()
data=data.split()
counter=0

for i in data:
    if i.endswith("big"):
        counter+=1
print(counter)
f.close()