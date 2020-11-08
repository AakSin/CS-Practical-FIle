f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.readlines()
counter=0
for i in data:
    i=i.lower()
    i=i.rstrip()
    if i[-1]=="." or i[-1]==",":
        i=i[:-1] #if the string has , or . in the end we remove it
    if i.endswith("free"):
        counter+=1 
print(counter)
f.close()