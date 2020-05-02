f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.read()
data=data[:-1] #remove fullstop in the end
data=data.replace(", "," ") #remove fullstop from the end of words
data=data.replace(". "," ") #remove comma from the end of words
data=data.lower()
data=data.split()
vowels=["a","e","i","o","u"]

for i in data:
    vc=0
    cc=0
    for j in i:
        if j.isalpha():
            if j in vowels:
                vc+=1
            else:
                cc+=1
    print(f"{i} has {vc} vowels and {cc} consonants")