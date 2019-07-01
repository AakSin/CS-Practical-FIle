import time
z= 1000000
a=[3]
f=open("primes.txt","w+")
f.write("2"+"\n")
n=3
k=time.time()
while n<=z:
    i=0
    while int(a[i])<=n**(1/2):
        if n%int(a[i])==0:
            break
        i+=1
    else:
        a.append(n)
        f.write(str(n)+"\n")
    n+=2
m=time.time()
f.close()
print(m-k)
print(len(a))