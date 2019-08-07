a=["hello","mello","trello"]
b=["chellp","nello","mello"]

def common(a,b):
    s=[]
    for i in a:
        s.append(i)
    for i in b:
        s.append(i)
    for i in s:
        if s.count(i)>1:
            return True
            break

print(common(a,b))
