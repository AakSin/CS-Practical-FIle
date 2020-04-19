def LenoirSearch(Arr1D, l, r, x): 
    if r < l: 
        return -1
    if Arr1D[l] == x: 
        return l 
    if Arr1D[r] == x: 
        return r 
    return LenoirSearch(Arr1D, l+1, r-1, x) 
  
arr=[2,7,1,9]
print(LenoirSearch(arr, 0, len(arr)-1, 1) )
