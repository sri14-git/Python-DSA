def binarySearch(arr,value,low,high):
    mid =low+(high-low)//2
    if low>high:
        return -1
    if arr[mid]==value:
        return mid
    elif arr[mid]<value:
        return binarySearch(arr,value,mid+1,high)
    elif arr[mid]>value:
        return binarySearch(arr,value,low,mid-1)   
arr=[1,2,3,4,5,6,7,8]
value=7
print(binarySearch(arr,value,0,len(arr)-1))