def selectionsort(arr):
    n=len(arr)
    for i  in range(n-1):
        min=arr[i]
        for j in range(1+i,n):
            if arr[j]< arr[i]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                min=arr[j]
            else: continue
    return(arr)
#
# 
# 
def bubblesort(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            else:continue
    return arr
print(bubblesort([13,46,24,52,20,9]))