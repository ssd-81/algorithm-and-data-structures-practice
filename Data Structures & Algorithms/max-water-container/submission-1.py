class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area calculation
        # min(height[j], height[i]) * j - i 

        # trying brute force 
        maxVol = 0 
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j-i)
                if maxVol < area:
                    maxVol = area
        return maxVol 