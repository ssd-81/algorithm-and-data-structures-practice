class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []
        def countHelp(x):
            count = 0

            while x >0:
                if x & 1 == 1:
                    count += 1
                x = x >> 1
            return count
        for i in range(n + 1):
            count.append(countHelp(i))
        return count