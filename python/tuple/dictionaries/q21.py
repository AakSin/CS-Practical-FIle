a=dict()
n=int(input('Enter the number of students'))
i=1
while i<=n:
    b=input('Enter the name of the student')
    c=float(input('Enter their percentage'))
    a[b]=c
    i+=1
print('Name of student','\t','percentage')
for i in a:
    print(i,'\t',a[i])
print('Do u want to delete a name of a student','yes=1','no=2',sep='\n')
h=int(input())
while h==1:
    x=input("which student's name do u want to delete")
    del a[x]
    print('Name of student','\t','percentage')
    for i in a:
        print(i,'\t',a[i])
    print('Do u want to delete a name of a student','yes=1','no=2',sep='\n')
    h=int(input())
if h==2:
    print('Name of student','\t','percentage')
    for i in a:
        print(i,'\t',a[i])
    print('do u want to quit','yes=1','no=2',sep='\n')
    j=int(input())
    if j==1:
        quit()
    else:
        print('What do u want to do with your life')
    
