lst=eval(input("enter a list"))
lst.sort()
print(lst)
n=len(lst)
if n%2!=0:
    print(lst[int(((n+1)/2)-1)])
else:
    print((lst[int((n/2))]+lst[int((n/2)-1)])/2)
