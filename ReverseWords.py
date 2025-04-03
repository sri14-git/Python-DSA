

s = "The quick brown fox"
# word=s.split()
# word=word[::-1]
# print(word)
i=0
j=0
ans=""
while i<len(s):
    while i <len(s) and s[i]==" ":
        i+=1
    j=i+1
    while j<len(s) and s[j]!=" ":
        j+=1
    if len(ans)!=0:
        ans=ans+" "+s[i:j]
    else:
        ans=ans+s[i:j]
    i=j+1
print(ans)