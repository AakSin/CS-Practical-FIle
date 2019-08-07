a=["hello","bello","hello","chello","tello","gello","bello"]
l=[]
for i in a:
    if i not in l:
        x=a.count(i)
        l.append(i)
        print(i ,"comes",x, " times")
