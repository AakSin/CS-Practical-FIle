ID= ["ADMIN","admin"]
PWD= "St0rE@1"
n=0
def login(uid,pwd):
        if pswd == PWD and userid in ID:
            return True
        if pswd != PWD or userid not in ID:
            return False
     
while n<=3:
    if n==3:
        print("Account Blocked")
        break
    userid=input("UserId:")
    pswd=input("Password:")
    if login(userid,pswd):
        print("login Successful")
        break
    else:
        print("Incorrect UserId or password")
        n+=1
        continue
