########################################-------RECURSION-------######################################
def printNos(n):
      if n==0:
            return
      print(n,end=" ")
      printNos(n-1)
        # Code here
#printNos(5)
def printn(n,num=1):
      if num<=n:
            print(num,end=" ")
            printn(n,num+1)
      else:
            return
#printn(5)
def sumoffirstn3(n,num=1,res=0):
      if n==0: return 0
      else:
        return n**3+sumoffirstn3(n-1)           
#sumoffirstn3(5)

def factorial(n,num=1):
      if num>=n:
            return num
      else:
            print(num,end=" ")
            return num*factorial(n,num+1)
#print(factorial(3))
def reverseArr(arr,n=0):
    l=len(arr)
    if n>=l//2:
         return arr
    arr[n],arr[l-n-1]=arr[l-n-1],arr[n]
    return reverseArr(arr,n+1)
#print(reverseArr([1,2,3,4,5]))
def removenonalpha(S:str):
    i=0
    while i < len(S):
            if not S[i].isalnum():
                S = S.replace(S[i], "")
                continue
            i += 1
    return S
def isPalindrome(S: str,n=0):
    i=0
    if not (S.isalnum() and S.islower()):
        i=0
        S=S.lower()
        while i < len(S):
            if not S[i].isalnum():
                S = S.replace(S[i], "")
                continue
            i += 1
    l =len(S)
    if n>=l //2 or l==1:
         return True
    if S[n]==S[l-n-1]:
         return isPalindrome(S,n+1)
    else: 
         return False

#print(isPalindrome("Nella's simple hymn: \"I attain my help, Miss Allen.\""))
def fib(n):
    if n==1:
          return 1
    if n==0:
         return 0
    else:
         return fib(n-1)+fib(n-2)
           
#print(fib(3))
################################################
def fib2(n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(2, n + 1):
            print("****",i)
            a, b = b, a + b
        return b
#print(fib2(2))
#################################################
def isorted(arr,l,r):
    if r>=len(arr):
        return True
    if r<len(arr):
        if arr[l]<arr[r]:
            return isorted(arr,l+1,r+1)
        else:
             return False
#print(isorted([1,3,2,5,6],0,1))
def linearsearch(arr,l,target):
     if l==len(arr):
          return False
     if arr[l]==target:
          return l
     else:
          return linearsearch(arr,l+1,target)
#print(linearsearch([1,2,3,4,5,6],0,7))
#### using an eztra variable
def removechr(s,l,n,target):
     res=""
     if l==n+1:
          ans=res
     if l<=n:
        if not s[l]==target:
            res+=(s[l])
            ans=removechr(s,l+1,n,target)
        else:
            ans=removechr(s,l+1,n,target)
     res+=ans
     return res
s="hello world"
print(removechr(s,0,len(s)-1,"l"))

##### without extra variable
def removechr1(s,l,n,target):
     res=""
     if l==n+1:
          return res
     if l<=n:
        if not s[l]==target:
            res+=(s[l])
            return res+removechr(s,l+1,n,target)
        else:
            return res+removechr(s,l+1,n,target)
s="hello world"
print(removechr(s,0,len(s)-1,"l"))