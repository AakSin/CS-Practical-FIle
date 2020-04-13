def RecurDigitSum(n):
    if (n%10==n):
        return n
    else:
        return n//10 + n%10
    
print(RecurDigitSum(45))
