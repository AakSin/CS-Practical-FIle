f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.read()
data = "".join(data.split()) #done to remove spaces
print(len(data))

f.close()