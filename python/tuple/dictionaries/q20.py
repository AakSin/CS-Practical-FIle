a=dict()
f=input('Which grade')
n=int(input('Enter the number of classes'))
i=1
while i<=n:
    b=input('Enter the class section')
    c=input('Enter the name of the class teacher')
    a[b]=c
    i+=1
print('Class','\t','Section','\t','Class teacher')
for i in a:
    print(f,'\t',i,'\t',a[i])

print('Do u want to know the class teacher of a section','Yes=1','No=2',sep='\n')
h=int(input())
while h==1:
    v=input('Enter the section')
    print('Class teacher is',a[v])
    print('Do u want to know the class teacher of a section','Yes=1','No=2',sep='\n')
    h=int(input())
if h==2:
    quit()

    


