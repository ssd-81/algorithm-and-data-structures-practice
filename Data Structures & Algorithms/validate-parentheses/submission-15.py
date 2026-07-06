class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {'{':'}', '(':')', '[':']'}
        stack = []
        for c in s:
            if c in bracket:
                stack.append(c)
            else:
                if not stack:
                    return False 
                if stack and bracket[stack[-1]] != c:
                    return False 
                stack.pop()
        return len(stack) == 0 