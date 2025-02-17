n=10

for i in range(1,n*2): 
    if i>n:
        print("*"*(n-1))
        n-=1
    else:
        print("*"*i)