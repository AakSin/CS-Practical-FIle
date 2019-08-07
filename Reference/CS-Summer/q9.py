# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. 
# The numbers obtained should be printed in a comma-separated sequence.
z=0
l=0
for i in range(100,401):
    l=i
    for j in range(3):
        k=l%10
        l=l//10
        if k%2==0:
            z=z+1
    if z==3:
        print(i)
    z=0


