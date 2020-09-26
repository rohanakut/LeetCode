class Solution:
    def myAtoi(self, str: str) -> int:
        final = []
        num = ['0','1','2','3','4','5','6','7','8','9']
        str = str.lstrip()
        flag = 0
        if(len(str) == 0 or str == '-+'):
            return 0
        if(str[0]=='-' or str[0]=='+'):
            if(str[0]=='-'):
                flag = 1
            str = str[1:]
        print(str)
        for i in range(len(str)):
            if(str[i] in num):
                final.append(str[i])
            else:
                break
        print(final)
        if(len(final)==0):
            #print("1")
            return 0
       # print(str,len(str))
       # num = ['0','1','2','3','4','5','6','7','8','9']
    #final = []
        #for i in range(len(str)):
         #   if(str[0] not in num):
          #      return 0
          #  if(str[i] in num):
          #      final.append(str[i])
          #  else:
          #      break
        s = ""
        s = s.join(final)
        num = int(float(s))
        if(flag == 1):
            num*=(-1)
        if(num>2147483647): 
            return (2147483647)
        if (num < -2147483648):
            return -2147483648
        else:
            return num