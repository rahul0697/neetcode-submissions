class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights)-1
        area = 0
        while(i<j):
            if heights[i]<=heights[j]:
                area = max(area, heights[i]*(j-i))
                i = i + 1
            elif heights[i]>heights[j]:
                area = max(area, heights[j]*(j-i))
                j = j - 1 
        return area
