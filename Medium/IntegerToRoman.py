class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = ["","I","II","III","IV","V","VI","VII","VIII","IX","X"]
        number_two = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC","C"]
        number_three = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM","M"]
        number_four = ["","M","MM","MMM"]
        ans = ''
        check = str(num)
        if(len(check)==4):
            ans = ans + number_four[int(num/1000)]
            num = num%1000
            ans = ans + number_three[int(num/100)]
            num = num%100
            ans = ans + number_two[int(num/10)]
            num = num%10
            ans = ans + numbers[int(num)]
        if(len(check)==3):
            ans = ans + number_three[int(num/100)]
            num = num%100
            ans = ans + number_two[int(num/10)]
            num = num%10
            ans = ans + numbers[int(num)]
            #num = num/10
        if(len(check)==2):
            ans = ans + number_two[int(num/10)]
            num = num%10
            ans = ans + numbers[int(num)]
            #num = num/10
        if(len(check)==1):
            ans = ans + numbers[int(num%10)]
            num = num/10
        return ans
            