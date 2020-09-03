class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        maxValue = 0
        mySet = set([])
        while(end<len(s)):
            if(s[end] not in mySet):
                mySet.add(s[end])
                end+=1
                maxValue = max(len(mySet),maxValue)
            else:
                mySet.discard(s[start])
                start+=1
        
        return maxValue

#This code does not make sense intuitively but we have to understand that this cpde is just calculating the *length* and not the actual substring        
# For example :
# substring  - "auryasgiwoa"
# In this the substring will be "auryasgiwo" . 
# Now if we run the code when the end pointer reaches position 10(last a) the set size is already  9. 
# Now ideally it should delete the 'a' at point 5 but what window does is it removes u from the list. 
# Now ideally the set should add two 'a''s in the set but the set never adds additional 'a' since the set stores only unique values. 
# So even though the end pointer is ad position 10 the size of the set will be 8 because of the set property.
        