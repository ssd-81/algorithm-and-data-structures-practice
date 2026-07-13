class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        next_warmer_day = [0] * len(temperatures)
        stack = []
        
        for idx in range(len(temperatures)-1, -1, -1):
            while stack and stack[-1][1] <= temperatures[idx]:
                stack.pop()
            
            if stack:
                next_warmer_day[idx] = stack[-1][0] - idx 

            stack.append((idx, temperatures[idx]))
        return next_warmer_day 