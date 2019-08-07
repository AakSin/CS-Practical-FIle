d1={"hello":"h","tello":"h","nello":"n","othello":"o","bello":"b","cello":"c","mello":"m","trello":"t"}
c=list(d1.items())
boo=False
d=len(c)
for i in range(0,d):
    for j in range(i+1,d):
        if c[i][1]==c[j][1]:
            boo=True
if boo==True:
    print("2 keys same value")
else:
    print("no same value")
