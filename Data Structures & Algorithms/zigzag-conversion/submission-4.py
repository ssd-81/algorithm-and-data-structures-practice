class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        inc = 2 * (numRows-1)

        for r in range(numRows):
            for j in range(r, len(s), inc):
                res += s[j]

                if r > 0 and r < (numRows-1) and j + inc - 2 * r < len(s):
                    res += s[j + inc - 2 * r]
        
        return res 