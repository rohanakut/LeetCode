class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        num = 0
        ref = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = num + ref[s[0]]
        i = i+1
        length = len(s)
        while(i<len(s)):
            if(s[i]=="M"):
                if(s[i-1]=="C"):
                    num = num+800
                else:
                    num = num +1000
               # num = num+1000
                print("entered M")
            if(s[i]=="C"):
                if(s[i-1]=="X"):
                    num = num+80
                else:
                    num = num + 100
                #num = num+100
                print("entered C")
            if(s[i]=="D"):
                if(s[i-1]=="C"):
                    num = num+300
                else:
                    num = num+500
                print("entered D")
            if(s[i]=="X"):
                if(s[i-1]=="I"):
                    num = num+8
                else:
                    num = num+10
                print("entered X")
            if(s[i] == "L"):
                if(s[i-1]=="X"):
                    num = num+30
                else:
                    num = num+50
                print("entered L")
            if(s[i]=="I"):
                num = num+1
                print("entered I")
            if(s[i]=="V"):
                if(s[i-1]=="I"):
                    num = num + 3
                else:
                    num = num+5
                print("entered V")
            print(num)
            i = i+1
        return num