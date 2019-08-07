#1-x1/2!+x2/3!-x3/4!+x4/5!...xn/(n+1)!
def fac(a):
    b=1
    for i in range(1,a+1):
        b*=i
    return b
n=2
x=5 
a=0
for i in range(1,n+2):
   if i%2==1:
       a+=(x**(i-1))/fac(i)
   else:
       a-=(x**(i-1))/fac(i)
   print(a)
    
print(a)

