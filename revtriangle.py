# Write your solution here.
n=5

# for i in range(1,n+1):
#     print(chr(64+i)*i)
#     print()

# for i in range(1,n*2,2):
#     print(" "*sp,"*"*i)
#     sp-=1
for i in range((n*2)-1,0,-2):
    sp=1
    if sp !=n-1:
        
        print(" "*sp,"*"*i)
        sp+=1