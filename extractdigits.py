import math
def extractdigits(n:int):
    count=int(math.log10(n)+1)
    cn=0
    arr=[]
    while n>0:
            if n%10!=0:
                arr.append(int(n%10))
                n=int(n/10)
                cn+=1
            elif n%10==0 and n>0:
                n=int(n/10)
                arr.append(0)
                cn+=1
            else:
                break
    print(arr[::-1])
    print("no of digit using log",count)
    print("no of digit without log",cn)
def addDigits(n: int) -> int:
    sum=0
    while n>0:
          if n%10 !=0:
               sum+=int(n%10)
               n=int(n/10)
    print(sum)
#addDigits(0)               
# 
# extractdigits(7)   
def reversenumber(n:int):
    revnum=0
    while n>0:
         ls=int(n%10)
         n=int(n/10)
         revnum=(revnum*10)+ls
    print(revnum)
# reversenumber(123)
def isPalindrome(n: int) -> bool:
        revnum=0
        num=n
        while n>0:
            ls=int(n%10)
            n=int(n/10)
            revnum=(revnum*10)+ls
        if (revnum)==(num):
            print("true")
            return True
        else:
            print("false")
            return False
# isPalindrome(121)
def armstrongnum(n:int):
     res=0
     num=n
     while n>0:
          ls=int(n%10)
          n=int(n/10)
          res=res+ls**3
     if res==num:
          print("armstrong number")
     else:
          print("Not armstrong number")
     
armstrongnum(1634)