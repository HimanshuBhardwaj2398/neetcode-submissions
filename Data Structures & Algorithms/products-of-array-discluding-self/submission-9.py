class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ## Reducing space complexity 

        ## storing prefix in first pass 

        n=len(nums)
        output=[0]*n
        prefix=1
    
        for i in range(n):
            output[i]=prefix
            prefix*=nums[i]
        ## now multiplying by the suffixes
        postfix=1
        for i in range(n-1,-1,-1):
            output[i]*=postfix
            postfix*=nums[i]
        return output 
            


        