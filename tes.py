def subset(arr,l,res=[]):
    if l>len(arr)-1:
        return res
    res.append(arr[l])
    left=subset(arr,l+1,res)
    res.pop()
    right=subset(arr,l+1,res)
    res.append(left[:])
    res.append(right[:])
    return res

arr=[1,2,3,4]
print(subset(arr,0))