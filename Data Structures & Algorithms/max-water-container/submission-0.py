class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right=0,n-1
        max_area=0
        while left<right :
            min_height=min(heights[left],heights[right])
            area=min_height*(right-left)
            if area>max_area:
                max_area=area
            if min_height==heights[left]:
                left+=1
            elif min_height==heights[right]:
                right-=1
            else:
                left+=1
                right-=1
        return max_area
                





        