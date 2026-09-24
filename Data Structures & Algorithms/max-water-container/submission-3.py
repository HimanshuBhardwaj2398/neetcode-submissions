class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right=0,n-1
        max_area=0
        while left<right :
            min_height=min(heights[left],heights[right])
            area=min_height*(right-left)
            max_area=max(max_area,area)
            if min_height==heights[left]:
                left+=1
            else :
                right-=1
        return max_area
                





        