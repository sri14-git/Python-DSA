def recursiveBubblesort(arr,l,r):
    if r==0:
        return
    if l<r :
        if arr[l]>arr[l+1]:
            arr[l],arr[l+1]=arr[l+1],arr[l]
        recursiveBubblesort(arr,l+1,r)
    else:
        recursiveBubblesort(arr,0,r-1)
    return arr
arr=[3,4,1,2]
print(recursiveBubblesort(arr,0,len(arr)-1))