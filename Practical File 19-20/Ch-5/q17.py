a=[4,5,6,4,1,3,4,56]
b=[]
for i in a:
    if i not in b:
        b.append(i)
        print(i,"appears",a.count(i),"times")
