f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.read()
data = "".join(data.split()) #done to remove spaces
lc=0 #lower character counter
uc=0 #upper character counter
for i in data:
    if i.islower():
        lc+=1
    elif i.isupper():
        uc+=1
print("the number of lower case characters are:",lc)
print("the number of upper case characters are:",uc)
