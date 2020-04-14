def RecurPow(x,n):
    if n==0:
        return 1
    else:
        return x*RecurPow(x,n-1)
print(RecurPow(5,2))