def BinarySearch (Arr1D, l, r, x): 
    if r >= l: 
  
        m = l + (r - l)//2
        if Arr1D[m] == x: 
            return m 
          
 
        elif Arr1D[m] > x: 
            return BinarySearch(Arr1D, l, m-1, x) 
  
        else: 
            return BinarySearch(Arr1D, m+1, r, x) 
  
    else: 
        return -1

Arr1D = [ 2, 3, 4, 10, 40 ] 

  
print(BinarySearch(Arr1D, 0, len(Arr1D)-1, 7) )