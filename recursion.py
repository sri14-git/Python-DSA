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
           
print(fib(3))
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
