# prime numbers

for i in range(2,30):
    for j in range(2,int(i**(1/2)+1)):
        if i%j==0:
            print(i, "not prime")
            break
    else:
        print(i,"prime")
