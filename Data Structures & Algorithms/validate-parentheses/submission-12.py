class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'(':')', '{':'}', '[':']'}
        for ch in s:
            if stack and stack[-1] in hashMap and ch == hashMap[stack[-1]]:
                stack.pop()
            else:
                stack.append(ch)

        return True if len(stack) == 0 else False