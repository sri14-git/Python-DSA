def recursiveSelectionSort(arr,l,r,min_idx=0):
    if l >= len(arr) - 1:
        return arr
    
    if r >= len(arr):
        arr[l], arr[min_idx] = arr[min_idx], arr[l]
        return recursiveSelectionSort(arr, l+1, l+2, l+1)
    
    if arr[r] < arr[min_idx]:
        min_idx = r
    
    return recursiveSelectionSort(arr, l, r+1, min_idx)
        
print(recursiveSelectionSort([52,2,10,1,48,5],0,1))
