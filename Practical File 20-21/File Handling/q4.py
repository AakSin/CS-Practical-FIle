f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.read()
data=data.lower()
vc=0
cc=0
vowels=["a","e","i","o","u"]
for i in data:
    if i.isalpha():
        if i in vowels:
            vc+=1
        else:
            cc+=1

print(vc,cc)

