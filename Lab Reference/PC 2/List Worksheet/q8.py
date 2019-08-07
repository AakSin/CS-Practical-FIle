s=["hello","mellow","card","bart"]
while True:
    a=input("enter word")
    if a=="0":
        break
    s.append(a)
a=[]
n=int(input("how many words should the smallest word have"))
print(len(s))
for i in range(len(s)):
    if len(s[i])<=n:
        a.append(s[i])

print(a)
