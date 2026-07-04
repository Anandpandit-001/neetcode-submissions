class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        area = 0

        while (l < r):
            current_area = min(heights[l] , heights[r]) * (r - l)

            if current_area > area:
                area = current_area
            
            if (heights[l] >= heights[r]):
                r = r - 1
            elif(heights[l] < heights[r]):
                l = l + 1

            
        return area