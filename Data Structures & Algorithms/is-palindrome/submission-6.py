class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_temp = ""
        for i in s:
            if i.isalnum():
                s_temp += i
        s_temp = s_temp.lower()


        for i in range(len(s_temp)):
            if(s_temp[i] != s_temp[len(s_temp)-1-i]):
                return False
        return True
        