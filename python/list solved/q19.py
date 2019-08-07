l=eval(input('Enter a list'))
for i in range(len(l)):
    if type(l[i])==int:
        if l[i]%2==0:
            l[i]=l[i]+10
        else:
            l[i]=l[i]+5
print(l)
