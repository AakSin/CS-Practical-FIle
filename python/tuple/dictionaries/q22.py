a=dict()
n=int(input('Enter the number of customers'))
i=1
while i<=n:
    b=input('Enter the name of the customer')
    c=input('Enter the items bought by the customer')
    d=float(input('Enter the cost of the items bought in dollars'))
    e=int(input('Enter their phone number'))
    a[b]=c,d,e
    i+=1
print('Name of customer','\t','items bought','\t','amount paid','\t','phone number')
for i in a:
    print(i,'\t',a[i])

    
