def bubbleSort(lst):
    print(lst)
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)
bubbleSort([56,23,89,71,43])
