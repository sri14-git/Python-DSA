def productExceptSelf(nums):
        pr=1
        p=[0 for i in range(len(nums))]
        for i in range(len(nums)):
            p[i]+=pr
            pr*=nums[i]
        pr=1
        for x in range(len(nums)-1,-1,-1):
            p[x]*=pr
            pr*=nums[x]
        return p
print(productExceptSelf([1,2,3,4]))