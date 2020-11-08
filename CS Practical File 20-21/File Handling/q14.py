f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.read()
data=data[:-1] #remove fullstop in the end
data=data.replace(", "," ") #remove fullstop from the end of words
data=data.replace(". "," ") #remove comma from the end of words
data=data.lower()
data=data.split()
vowels=["a","e","i","o","u"]
dict={} #dictionary for storing words and the number of vowels they have

for i in data:
    vc=0
    for j in i:
        if j.isalpha():
            if j in vowels:
                vc+=1
    dict[i]=vc
print(max(dict, key=dict.get))
f.close()