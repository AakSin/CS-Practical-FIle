def RecurDigitSum(n):
    if (n%10==n):
        return n
    else:
        return RecurDigitSum(n//10) + RecurDigitSum(n%10)
    
print(RecurDigitSum(1111))
