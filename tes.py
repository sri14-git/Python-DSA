
# def triangle(r,c=0):
#     if (r==0):
#         return
#     if c<r:
#         print("*",end="")
#         triangle(r,c+1)
        
#     else:
#         print()
#         triangle(r - 1, 0)
        
    
# triangle(4)
def recursiveBubblesort(arr,l,r):
    if r==0:
        return
    if l<r-1 :
        if arr[l]>arr[l+1]:
            arr[l],arr[l+1]=arr[l+1],arr[l]
        recursiveBubblesort(arr,l+1,r)
    else:
        recursiveBubblesort(arr,0,r-1)
    return arr
arr=[3,4,1,2]
print(recursiveBubblesort(arr,0,4))