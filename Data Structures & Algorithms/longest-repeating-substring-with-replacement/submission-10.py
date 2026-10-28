class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best,left=0,0
        counts={}
        for right,ch in enumerate(s):
            counts[ch]=counts.get(ch,0)+1
            while (right-left+1)-max(counts.values())>k:
                counts[s[left]]-=1
                left+=1
            best=max(best,(right-left+1))
        return best

            
        