class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best,left=0,0
        counts={}
        for right,ch in enumerate(s):
            counts[ch]=counts.get(ch,0)+1
            win_len= right-left+1
            max_count=max(counts.values())
            while win_len - max_count > k:
               counts[s[left]]=counts.get(s[left],0)-1
               left+=1
               win_len=right-left+1
               max_count=max(counts.values())
               rep_needed=win_len - max_count
            best=max(best,win_len)
        return best 


               

           
        