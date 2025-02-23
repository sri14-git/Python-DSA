def mergesort(arr,low,high):
    if low>=high:
        return
    mid=int((high+low)/2)
    mergesort(arr,low,mid)  #[13,46,24,20,9]
    # 13,46
    # 13 
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)




def merge(arr,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    while left<=mid and right<=high:
        if arr[left]< arr[right]:

            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
arr=[13,46,24,52,20,9]
print(mergesort(arr,0,5))
print(arr)

