class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for n in nums: 
            if n-1 not in nums: 
                current=1
                next_number=n+1
                while next_number in nums:
                    current+=1
                    next_number+=1
                longest=max(current,longest)
        return longest 
            



         



        