class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashNum={}
        for i,num in enumerate(nums):
            if target-num in HashNum and ( HashNum[target-num]!=i):
                return [HashNum[target-num],i]
            HashNum[num]=i
        
        
        