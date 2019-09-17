lst=[32,21,17,29,14]

for i in range(1,len(lst)):
    for j in range(i,0,-1):
        if lst[j-1]>lst[j]:
            lst[j],lst[j-1]=lst[j-1],lst[j]
        else:
            break
    print(lst)
    

"""
data_list=[32,21,17,29,14]
for k in range(1,len(data_list)):

        t=data_list[k]

        ptr=k-1

        while(ptr>=0)and data_list[ptr]>t:
            data_list[ptr+1]=data_list[ptr]
            ptr=ptr-1
        else:
            data_list[ptr+1]=t
        print(data_list)
"""
