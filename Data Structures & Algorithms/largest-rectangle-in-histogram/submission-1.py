class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = float('-inf')
        temp = 0 
        for i, height in enumerate(heights):
            if stack:
                temp = i 
                while stack and stack[-1][0] > height:
                    last_height, idx = stack.pop()
                    max_area = max(last_height * (i - idx), max_area)
                    temp = idx
                stack.append((height, temp))
            else:
                stack.append((height, i))
        n = len(heights)
        while stack:
            threshold_height, idx = stack.pop()
            max_area = max(max_area, threshold_height * (n - idx))
        return max_area 