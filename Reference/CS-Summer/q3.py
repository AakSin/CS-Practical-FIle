# 3. Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for row in range(1,10):
    for col in range(5):
        if (row<6 and col<row) or (row>5 and col<10-row):
            print("*",end="")
    print()