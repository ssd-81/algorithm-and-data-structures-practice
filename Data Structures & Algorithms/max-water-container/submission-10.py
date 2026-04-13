class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        curMaxVolume = 0
        
        while l < r:
            newVol = min(heights[l], heights[r]) * (r - l)

            curMaxVolume = max(newVol, curMaxVolume)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return curMaxVolume  