class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = float('-inf')
        temp = 0 
        for i, height in enumerate(heights):
            start = i 
            while stack and stack[-1][0] > height:
                last_height, idx = stack.pop()
                max_area = max(max_area, last_height * (i - idx))
                start = idx
            stack.append((height, start))
        n = len(heights)
        while stack:
            threshold_height, idx = stack.pop()
            max_area = max(max_area, threshold_height * (n - idx))
        return max_area 