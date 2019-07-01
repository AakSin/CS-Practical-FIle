
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 

for i in range(1500,2701):
    if i%5==0 and i%7==0:
        print(i)

# prime numbers

for i in range(2,30):
    for j in range(2,int(i**(1/2)+1)):
        if i%j==0:
            print(i, "not prime")
            break
    else:
        print(i,"prime")
