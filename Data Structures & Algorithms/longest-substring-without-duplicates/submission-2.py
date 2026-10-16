class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, best=0,0 
        window=set()
        for right,ch in enumerate(s):
            while ch in window: 
                window.remove(s[left])
                left+=1
            window.add(ch)
            best=max(best,right-left+1)
        return best





        