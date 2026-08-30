class Solution:
    def productExceptSelf(self, nums: List[int]) ->List[int]:

        n=len(nums)
        zero_count=0
        res = [0]*n
        non_zero_product=1
        for i in range(n):
            if nums[i]==0:
                zero_count+=1
                continue
            non_zero_product*=nums[i]
        if zero_count >1 : return res

        for i,c in enumerate(nums):
            if zero_count : 
                res[i]=0 if c else non_zero_product
            else:
                res[i]=non_zero_product//c
        return res


        

        
            