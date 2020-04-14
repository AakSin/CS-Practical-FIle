def LenoirSearch(Arr1D, l, r, x): 
    if r < l: 
        return -1
    if arr[l] == x: 
        return l 
    if arr[r] == x: 
        return r 
    return LenoirSearch(arr, l+1, r-1, x) 
  
arr=[2,7,1,9]
print(LenoirSearch(arr, 0, len(arr)-1, 7) )
