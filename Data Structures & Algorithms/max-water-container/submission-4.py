class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right=0,n-1
        max_area=0
        while left<right :
            left_h,right_h=heights[left],heights[right]
            min_height=min(left_h,right_h)
            area=min_height*(right-left)
            max_area=max(max_area,area)
            if min_height==left_h:
                left+=1
            else :
                right-=1
        return max_area
                





        