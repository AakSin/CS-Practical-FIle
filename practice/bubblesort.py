lst=[32,21,17,29,14]


for i in range(len(lst)-1,0,-1):
    
    for j in range(i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1], lst[j]
        else:
            continue
    
