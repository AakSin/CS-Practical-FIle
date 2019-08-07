d1={"hello":"h","nello":"m","cheelo":"c","nibba":"n"}
d2={"trello":"t","hello":"h","nello":"n","sello":"s"}
a=d1.keys()
b=d2.keys()
for i in a:
    if i in b:
        print(i)
