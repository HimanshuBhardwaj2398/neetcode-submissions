class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): 
            j_value=target-nums[i]
            if j_value in nums : 
                j=nums.index(j_value)
                if i!=j:
                    return sorted([i,j])          

        