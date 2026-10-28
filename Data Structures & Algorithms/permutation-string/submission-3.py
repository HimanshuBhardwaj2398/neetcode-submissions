class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        s1_chars=set(s1)
        counts_s1=Counter(s1)
        left=0
        while left+n1<=n2:
            window=s2[left:left+n1]
            for i,ch in enumerate(window):
                if ch not in s1_chars:
                    left+=i+1
                    break
            else: 
                counts_s2=Counter(window)
                if counts_s1==counts_s2:
                    return True
                left+=1
        return False

        