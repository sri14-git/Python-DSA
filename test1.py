from typing import Counter

res=[]
arr=[5,5,4,6,4]
freq=[[] for i in range(len(arr))]
count1=Counter(arr)
count1=dict(sorted(count1.items()))
# for i,c in count1.items():
#         freq[c].append(i)
# for i in range(len(freq)-1,-1,-1):
#     for x in freq[i]:
#         res.append(x)
# print(res)
print(Counter(count1.items()))