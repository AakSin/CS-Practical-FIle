def insertion_sort(data_list):
    for k in range(1,len(data_list)):
        t=data_list[k]
        ptr=k-1
        while(ptr>=0)and(data_list[ptr]>t):
                    data_list[ptr+1]=data_list[ptr]
                    ptr=ptr-1
        else:
            data_list[ptr+1]=t
        print(data_list)
a=[31,89,20,159,15]
print(insertion_sort(a))
                        
