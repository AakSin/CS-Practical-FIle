def insertion_sort(lst):
    for k in range(1,len(lst)):
        t=lst[k]
        ptr=k-1
        while(ptr>=0)and lst[ptr]>t:
            lst[ptr+1]=lst[ptr]
            ptr=ptr-1
        else:
            lst[ptr+1]=t
    print("sorted",lst)

insertion_sort([31,19,28,42,7])
