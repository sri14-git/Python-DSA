def freqinarray(arr):
    dic={}
    count=0
    res=[]
    for i in range(1,len(arr)+1):
        dic[i]=count
    for x in arr:
        dic[x]+=1
    for x in dic.values():
        res.append(x)
    print(res)
#freqinarray([3, 3, 3, 3])
def grpanagrams(arr):
    dic={}
    res=[]
    for s in arr:
        sor=sorted(s)
        dic[tuple(sor)]=[]
    for i in arr:
        sor=sorted(i)
        dic[tuple(sor)].append(i)
    for i in dic.keys():
                res.append(dic.get(i))
    return res

def twosums(nums,target):
        dic={}
        for i,n in enumerate(nums):
            diff =target-n
            if diff in dic:
                return [dic[diff],i]
            dic[n]=i
        return  