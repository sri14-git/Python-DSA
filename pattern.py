def symspures(n):
      def spures(n:int):
            sp=int((n*2)/2)
            for i in range(1,n*2,2):
                  print(" "*sp+"*"*i)
                  sp-=1   
      def revspures(n:int):
            sp=2
            l=(n*2)-1
            for i in range(l-1,0,-2):
                  print(" "*sp+"*"*(i-1))
                  sp+=1
      spures(n)
      revspures(n)
def mirroralpha(n:int):
      sp=int((n*2)/2)-1
      for i in range(n):
            if i<n:
                  while True:
                        print(f" "*sp,end="")
                        break
                  sp-=1 
            for y in range(2*i+1):
                  if y<=((i*2)/2):
                        ch=65+y
                        print(chr(ch),end="") 
                  else:
                        ch -=1
                        print(chr(ch),end="")
                  
            print()
            

# symspures(5)
#mirroralpha(4)
def alphaTriangle(n: int):
    ch=65+n
    for i in range(1,n+1):
      for x in range(ch-i,ch):                  
# E 
# D E 
# C D E 
# B C D E 
# A B C D E 
            print(chr(x)+" ",end="")
      print()
#alphaTriangle(5)

def betatriangle(n):
      ch=64+n
      for i in range(1,n+1):
            for x in range(ch,ch-i,-1):
                  print(chr(x)+' ',end="")
            print()

#betatriangle(4)
# n=5
# num=n*2
# sp=0
# for i in range(n*2):
#       for x in range(i,0,-1):
#             if i==0 | i ==((n*2)-1):
#                   print("*"*n*2+' ',end="")
#             elif i<=n:

def insiderombus(n):
    num=n
    l=(n*2)-2
    md=int((n*2)/2)
    sp=0
    for x in range(num*2):
        if (x==0) or x ==(num*2)-1:
                print("* "*(num*2))
        if x<md-1:
                if sp<l:
                    sp+=2
                print("* "*(n-1)+"  "*sp+" *"*(n-1))
                n-=1
        elif x>md-1 and x<((num*2)-1):
            if n<=num:
                print("* "*(n)+"  "*sp+" *"*(n))
            sp-=2
            n+=1
def mirrortriangle(n):
      l=(n*2)-2
      sp=l
      for i in range(1,n*2): 
            if i>n:
                  if sp<=l:
                        sp=sp+2
                  print("*"*(n-1)+" "*sp+"*"*(n-1))
                  n-=1
                  
            else:
                  print("*"*i+" "*sp+"*"*i)
                  if sp>0:
                        sp-=2
#mirrortriangle(5)

def rectange(n):
      sp=n-2
      for i in range(n):
            if i ==0 or i == n-1:
                  print("*"*n)
            else:
                  print("*"+" "*sp+"*")
#rectange(5)
def incnumbertriangle(n:int):
      res=1
      for i in range(1,n+1):
            for x in range(i):
                  print(res,end="")
                  res+=1
            print()
#incnumbertriangle(4)
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
      if n>0:
            res=res+(num**3)
            return sumoffirstn3(n-1,num+1,res)
      else:
            return res
            
#sumoffirstn3(5)

def factorial(n,num=1):
      if n ==1:
            print(1)
            return
      else:
            if num<=n:
                  print(num,end=" ")
                  num=num*(num+1)
                  factorial(n,num)
                  
            else:
                  return
factorial(250)