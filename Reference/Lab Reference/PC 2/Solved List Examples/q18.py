a=[4,55,6,323,3221]
n=7
def exist(a):
    for i in a:
        if i==n:
            return "exists"
            break
    else:
        return "doesn't exist"

print(exist(a))
