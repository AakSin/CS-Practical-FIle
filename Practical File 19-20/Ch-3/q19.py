#1-x2/4!+x3/6!-x4/8!+x5/10!...xn/(2n)!
def fac(a):
    b=1
    for i in range(1,a+1):
        b*=i
    return b
n=4
x=4 
a=1
for i in range(2,n+1):
   if i%2==1:
       a+=(x**(i))/fac(i*2)
   else:
       a-=(x**(i))/fac(i*2)
   print(a)
    
print(a)

