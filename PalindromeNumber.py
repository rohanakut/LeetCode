class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s1 = s[::-1]
       # print(s1,s)
        if(s == s1):
            return 1
        else:
            return 0