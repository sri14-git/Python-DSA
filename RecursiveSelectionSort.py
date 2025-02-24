# def RecursiveSelectionSort(arr, l, r, min=0):
#     if l>=len(arr)-1:
#         return 
#     if l<r:
#         if r==len(arr) :
#             RecursiveSelectionSort(arr,l+1,l+2,min+1)
#         if arr[r]<arr[min]:
#             arr[r],arr[min]=arr[min],arr[r]
#             min=l
        
#     RecursiveSelectionSort(arr,l,r+1,min)
        
#     return arr
# # Example usage
# arr=[13, 12, 24, 52, 20, 9]
# print(RecursiveSelectionSort(arr, 0, 1))
def RecursiveSelectionSort(arr, l, r, min_idx=0):
    # Base condition: stop recursion when the left index reaches the end of the array
    if l >= len(arr) - 1:
        return arr
    
    # If the right index reaches the end of the array, swap the minimum element with the current left index
    if r >= len(arr):
        arr[l], arr[min_idx] = arr[min_idx], arr[l]
        # Move to the next unsorted portion of the array
        return RecursiveSelectionSort(arr, l + 1, l + 2, l + 1)
    
    # Find the index of the minimum element in the unsorted portion of the array
    if arr[r] < arr[min_idx]:
        min_idx = r
    
    # Recursively move the right index to find the minimum element
    return RecursiveSelectionSort(arr, l, r + 1, min_idx)

# Example usage
arr = [13, 12, 24, 52, 20, 9]
print(RecursiveSelectionSort(arr, 0, 1))