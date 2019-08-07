d1={'hello':'h','tree':'t','atelo':'a','lello':'l'}
d2={'lello':'l','mello':'m','chetto':'c','hello':'h'}
a=d1.keys()
b=d2.keys()
for i in a:
    if i in b:
        print(i)
    
