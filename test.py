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
# def topKFrequent(nums, k: int):
#         dic={nums[i]:0 for i in range(len(nums))}
#         res=[]
#         for i in nums:
#             dic[i]+=1
#         if len(nums)==k:
#             nums=set(nums)
#             return list(nums)
#         else:
            
#         return res
arr=[1,2,33,4,5]
dic={i:k for i in arr and for k in len(arr)-1 k+=1}