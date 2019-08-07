
lst=[]
lst1=[]
lst2=[]
for i in range(1,21):
    lst.append(i)
for i in range(5,16,2):
    lst1.append(lst[i])
for i in range(0,20,4):
    lst2.append(lst[i])
   
print(sum(lst1))
print(sum(lst2)/len(lst2))
    
