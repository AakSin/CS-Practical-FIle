a={'hello':'h','tree':'t','atelo':'a','lello':'l'}
c=-1
for i in a:
    k=a[i]
    for j in a:
        if a[j]==k and j!=i:
            c=0
            print("two keys have same value")
            break
    if c==0:
        break
if c!=0:
    print("no keys have same value")
