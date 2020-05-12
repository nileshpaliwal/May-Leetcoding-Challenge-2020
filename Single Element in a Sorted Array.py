#You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
#
# 
#
#Example 1:
#
#Input: [1,1,2,3,3,4,4,8,8]
#Output: 2
#Example 2:
#
#Input: [3,3,7,7,10,11,11]
#Output: 10


class Solution(object):
    def singleNonDuplicate(self, nums):
        
        dictionary = {}

        for i in nums:
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1
            if dictionary[i]==2:
                del dictionary[i]

        for i in dictionary:
            return(i)