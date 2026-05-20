class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums: 
            count[num]=count.get(num,0)+1
        
        count=sorted(count.items(),key=lambda kv: kv[1],reverse=True)

        result=list(kv[0] for kv in count)
        return result[:k]


        