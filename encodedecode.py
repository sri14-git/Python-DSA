def encode(strs) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s # 4#neet4#code4#love3#you
        return res
        

def decode(s: str):
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#": ### need to use while coz if we use if -- if the integer is double or anything more it does work coz if statement doesnt loop till we get # 
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+length+1])
            i=j+length+1
        return res
print(decode(encode(["we","say",":","yes","!@#$%^&*()"])))