class Solution:
    def performOperation(self, a, b , op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b 
        elif op == '*':
            return a * b
        elif op == '/':
            if a * b < 0:
                return ceil(a / b)
            return a // b 

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set(['+', '-', '/', '*'])
        res = 0 

        for c in tokens:
            if c in op:
                b = stack.pop()
                a = stack.pop()
                res = self.performOperation(a, b, c)
                print("stack", stack)
                print(f"a: {a}, b:{b}, op:{c}")
                stack.append(res) 
            else:
                stack.append(int(c))
        return stack[-1] 