x=0 #savings amount
y={} #accholderinfo
while True:
    s=input("would you like to open a savings account? (enter yes or no): ")
    if s=="yes":
        name=input("enter account holders name: ")
        panno=input("enter account holders pan card number: ")
        pswd=input("enter 4 digit pin for account: ")
        y[name]=pswd
    break
    if s=="no":
        continue
while True:
    p=input("enter the follwing to choose action: \n 1) Deposit to deposit money into saving account\n 2) Withdrawal to withdraw from saving account \n 3) FD to create a fixed deposit \n 4) EXIT to exit \n :")
    z=p.lower()
    if z=="deposit":
        depAmnt=int(input("enter amount to deposit in rupees: "))
        if depAmnt<10000:
            print("minimum balance for savings account is 10000")
        if depAmnt>=10000:
            x+=depAmnt
            print("your savings account balance is: ",x)
    if z=="withdrawal":
        withdAmnt=int(input("enter amount to withdraw in rupees"))
        if x-withdAmnt<10000:
            print("minimum balance for savings acount is 10000")
        if x-withdAmnt>=10000:
            x-=withdAmnt
            print("your balance is: ",x)
    if z=="fd":
        fdAmnt=int(input("enter amount in rupees: "))
        if fdAmnt<100000:
            print("minimum amount for a fixed deposit is 100000")
        period=int(input("enter maturity time in months: "))
        if period<6:
            print("minimum fixed deposite period is 6 months")
        elif 6<period<=12:
            fdAmnt+=fdAmnt*0.044
            print("the maturity amount is ", fdAmnt)
        elif 12<period<=36:
            fdAmnt+=fdAmnt*0.051
            print("the maturity amount is ", fdAmnt)
        elif 36<period<=60:
            fdAmnt+=fdAmnt*0.053
            print("the maturity amount is ", fdAmnt)
        elif 60<period<=120:
            fdAmnt+=fdAmnt*0.055
            print("the maturity amount is ", fdAmnt)
    if z=="exit":
        break
