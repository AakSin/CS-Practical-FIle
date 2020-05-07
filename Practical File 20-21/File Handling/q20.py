f=open("Practical File 20-21\\File Handling\\texts\\read_sample.txt","r")
data=f.readlines()
counter=0
for i in data:
    i=i.lower()
    for j in range(len(i)-1,-1,-1): #we start iterating backwards in each line using this loop. j is an integer and has been used to represent the index of characters.
        if i[j].isalnum(): #we check if the character we are encountering is alpha numeric or not. This is done to ignore /n or ., etc.
            if i[j]=="t": #if the encountered alpha numeric character is t then we add it to the counter
                counter+=1
            break #if the encounter alpha numeric counter is not t then we break the loop because we are looking for an alpha numeric character using the #j loop.
print(counter)
f.close()