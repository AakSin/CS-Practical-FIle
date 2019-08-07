import time
z=0
p=time.time()
while True:
    for i in range(1,20):
        print("*"*i)
    for j in range(18,0,-1):
        print("*"*j)
    z+=1
    if time.time()-p>=15:
        break
print(z)
