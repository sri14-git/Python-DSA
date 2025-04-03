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

def insertionsort(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr
print(insertionsort([52,2,10,1,48,5]))