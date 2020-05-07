f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.read()
spc=0 #space character counter
syc=0 #symbol character counter
dc=0 #digitcounter
for i in data:
    if i.isalnum():
        if i.isdigit():
            dc+=1
    else:
        if i.isspace():
            spc+=1
        else:
            syc+=1

print(syc,spc,dc)

f.close()