n=23
k=int((n/2)+1)
bl=" "
z=2*k-1
for i in range(1,n+1):
    if i<=k:
        print((bl*(k-i))+ ("*"*(2*i-1)) + (bl*(k-i)))
    else:
        z=z-2
        print((bl*(i-k)) + ("*"*(z)) + (bl*(i-k)))
