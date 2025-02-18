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
print(factorial(3))