def sumoffirstn3(n):
    if n==0: return 0
    else:
        return n**3+sumoffirstn3(n-1)
    
print(sumoffirstn3(5))
