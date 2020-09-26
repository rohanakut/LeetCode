class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if(x<0):
            flag = 1
            x *= (-1)
        s = str(x)
        s = s[::-1]
        x = int(s)
        #print(s,x)
        if(x>2147483648):
            return 0
        if(flag == 1):
            x*=(-1)
        return x
        