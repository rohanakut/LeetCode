class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        #print(nums)
        #result = []
        result1 = 100000
        value = 0
        #print(nums)
        for i in range(0,len(nums)-1):
            num = nums[i]
            a = i+1
            b = len(nums)-1
            flag = 0
            check = target
            while(a<b):
                value = nums[a]+nums[b]+nums[i]
                #print(nums[i],nums[a],nums[b],value)
                if(nums[a]+nums[b]+nums[i]<check):
                    a = a+1
                    #print("in")
                elif(nums[a]+nums[b]+nums[i]>check):
                    b = b-1
                elif(nums[a]+nums[b]+nums[i]==check):
                    return target
                
                if(target>0):
                    if(value<=0):
                        #result.append([target+(-1)*value,value])
                        result = target+(-1)*value
                        if(result<0):
                            reuslt = result *(-1)
                        
                    elif(value>0):
                        final = target - value
                        if(final<0):
                            final = final *(-1)
                        result = final
                elif(target<=0):
                    if(value<=0):
                        final = target*(-1) - value*(-1)
                        if(final<0):
                            final = final *(-1)
                        result = final
                    elif(value>0):
                        #result.append([target+(-1)*value,value])
                        result = target*(-1)+value
                        if(result<0):
                            reuslt = result *(-1)
                #print(result,result1)
                print("      ")
                if(result<result1):
                    result1 = result
                    value1 = value
                    flag = 1
                if(flag==1 and result>result1):
                    break
        
        return(value1)