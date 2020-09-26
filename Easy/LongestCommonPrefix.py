class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
            
        strs.sort(key = len)
        print(strs)
        i = 0
        result = ""
        if(len(strs)==0):
            return result
        if(len(strs)==1):
            return strs[0]
        str1 = strs[0]
        str2 = strs[1]
        print(str1,str2)
        for i in range(len(str1)):
            if(str1[i]==str2[i]):
                #print(str1[i],str2[i])
                result = result + str1[i]
            else:
                break
        if(len(result)==0):
            return result
        print(result)
        i = 2
        while(i<len(strs)):
            str1 = strs[i]
            print(str1,i)
            #str2 = strs[i+1]
            j = 0
            if(result[0]==str1[j]):
                j = 1
                while(j<len(result)):
                    if(str1[j]==result[j]):
                        j = j+1
                    else:
                        print(str1[j])
                        result = result[0:j]
            else:
                result = ""
                break
            i = i+1
        print(result)
        return(result)
                
        