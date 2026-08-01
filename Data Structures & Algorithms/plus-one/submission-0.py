class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        carry = 1

        for i in range(len(digits)-1,-1,-1):
            val = digits[i] + carry 
            digits[i] = (val)% 10 
            carry = val // 10 
        digits = digits[::-1]
        if carry != 0:
            digits.append(carry)
        return digits[::-1]