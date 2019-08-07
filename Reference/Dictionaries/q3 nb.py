months={"january":31,"february":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
############################
while True:
    a=input("What month's days do you want to know (Please enter in small and enter the complete name) --use 0 to break the loop :")
    if a=="0":
        break
    print(a,"has",months.get(a),"days")
##############################################
alphkeys=list(months.keys())
alphkeys.sort()
print(alphkeys)
    
########################
for i in months:
    if months.get(i)==31:
        print(i)

#######################

pairs=list(months.items())
c=len(pairs)

for i in range(0,c):
    for j in range(i+1,c):
        if pairs[i][1]>pairs[j][1]:
            pairs[i],pairs[j]=pairs[j],pairs[i]

print(pairs)
