class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        n1,n2=len(s1),len(s2)
        counts_s1={}
        for ch in s1:
            counts_s1[ch]=counts_s1.get(ch,0)+1
        while left+n1<=n2:
            counts_s2={}
            for i,ch in enumerate(s2[left:left+n1]):
                if ch not in s1:
                    left+=i+1
                    break
                counts_s2[ch]=counts_s2.get(ch,0)+1
            else:
                if counts_s2==counts_s1:
                    return True
                left+=1
        return False 

            



        