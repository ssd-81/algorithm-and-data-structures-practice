class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {')':'(', ']': '[', '}':'{'}
        for char in s:
            print(stack[-1])
            if stack and stack[-1] in hashMap and stack[-1] == hashMap[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)

        return True if len(stack) == 0 else False