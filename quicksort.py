def partition(arr,low,high): ##### with o(1) space complexity
    i=low
    j=high
    pivot=low
    while(i<j):
        while(arr[i]<=arr[pivot] and i<high):
            i+=1
        while (arr[j]>arr[pivot] and j>low):
            j-=1
        if i<j:
            arr[j],arr[i]=arr[i],arr[j]
    arr[pivot],arr[j]=arr[j],arr[pivot]
    return j

def qs(arr,low,high):
    if low<high:
        pivot= partition(arr,low,high)
        qs(arr,low,pivot-1)
        qs(arr,pivot+1,high)
    return arr
arr=[13,46,24,52,20,9]

def quicks(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[i for i in arr[1:] if i<=pivot]
    right=[x for x in arr[1:] if x>pivot]
    return quicks(left)+[pivot]+quicks(right)
print(qs(arr,0,len(arr)-1))