# nums=[1,1,1,2,2,3]
# k=2
# dic={}
# num=set(nums)
# count=1
# res=[]
# for i in num:
#     dic[i]=count
# for i in nums:
#     if dic[i]:
#         dic[i]+=1
# for key,values in dic.items():
#     print(dic[key])
#     if values>=k:
#         res.append(key)

#print(res)    
# 
# 
#         ###leetcode

arr=[1,2,3,4,5]
for i,n in enumerate(arr):
    print(i,n)

def topKFrequent(nums, k: int):
    dic={i:0 for i in nums }
    freq=[[] for i in range(len(nums)+1)]
    for i in nums:
        dic[i]+=1
    for n,c in dic.items():
        freq[c].append(n)
    res=[]
    for i in range(len(freq)-1,0,-1):
        if len(res)<k:
            for x in freq[i]:
                res.append(x)
        
    return res

        




print(topKFrequent([1,2,2,3,3,3],2))