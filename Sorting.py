def selectionsort(arr):
    for i in range(len(arr)):
        min=i
        j=i
        while j <len(arr):
            if arr[j]<arr[min]:
                min=j
            j+=1
        arr[i],arr[min]=arr[min],arr[i]
    return arr

# 
def bubblesort(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp    
    return arr
def insertionsort(arr):
    for i in range(len(arr)-1):
        j=i
        while j>0 and arr[j-1]> arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    

print(bubblesort([13,46,24,52,20,9]))