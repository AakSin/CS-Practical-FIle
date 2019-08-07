l1=[1,3,4,1,5,7,9,7]
l2=[]
l3=[]

for i in l1:
    if l1.count(i)>1 :
        l2.append(i)
    else:
        l3.append(i)

print(l2, " - duplicates")
print(l3, " - unique" )
