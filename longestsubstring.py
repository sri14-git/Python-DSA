def longestsubstring(s):
        charset=set()
        maxsub=0
        l=0
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[i])
            maxsub=max(maxsub,(i-l)+1)
            
        return maxsub
print(longestsubstring("pwwkew"))