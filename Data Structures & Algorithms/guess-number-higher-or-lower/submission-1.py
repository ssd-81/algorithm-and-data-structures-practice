# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # what am I trying to do here
        # i am try to find a number in the range 1-n 
        # we do not know which num it is 
        # but we will get a feedback on each choice
        # so we are using binary search pattern to find the num in least steps
        
        low = 1
        high = n 
        while low <= high:
            mid = low + (high - low) // 2

            if guess(mid) == -1:
                high = mid - 1
            elif guess(mid) == 1:
                low = mid + 1
            else:
                return mid
        