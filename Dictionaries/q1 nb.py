d1={"hello":"h","mello":"m","nello":"n","othello":"o"}
d2={"bello":"b","cello":"c","mello":"m","trello":"t"}
key1=list(d1.keys())
key2=list(d2.keys())

for i in key1:
    if i in key2:
        print(i)