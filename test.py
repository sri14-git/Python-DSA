def isPalindrome(S: str,n=0):
    i=0
    S = S.lower()
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

print(isPalindrome("aA"))
    
     