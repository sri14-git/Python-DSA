


from collections import Counter
from operator import le


s = " The quick brown fox "
# # word=s.split()
# # word=word[::-1]
# # print(" ".join(word))
# i=0
# j=0
# ans=""
# while i<len(s):
#     while i <len(s) and s[i]==" ":
#         i+=1
#     j=i
#     while j<len(s) and s[j]!=" ":
#         j+=1
#     if len(ans)!=0:
#         ans=s[i:j]+" "+ans
#     else:
#         ans=s[i:j]+ans
#     i=j
# print(ans)
# res=[]
# kpair=[]
k=3
arr=[1,1,2,7,11]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         res.append([arr[i],arr[j]])
# print(res)
# for i in range(len(res)-1,0,-1):
#     for j in range(0,i):
#         if sum(list(res[j])) > sum(list(res[j+1])):
#             res[j],res[j+1]=res[j+1],res[j]
# l=0
# while k!=0 and l<len(res):
#     if sorted(res[l]) not in kpair:
#         kpair.append(res[l])
#         k-=1
#     l+=1
# print(kpair)

# import heapq
# heap=[]
# res=[]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         pair=(arr[i],arr[j])
#         heapq.heappush(heap,(sum(pair),[arr[i],arr[j]]))
# print(heap)
# while k!=0 and len(heap)>=k:
#     res.append(heapq.heappop(heap)[1])
#     k-=1

# print(res)
