class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_temp = ""
        for i in s:
            if i.isalnum():
                s_temp += i
        s_temp = s_temp.lower()


        return s_temp == ''.join(reversed(s_temp))
        