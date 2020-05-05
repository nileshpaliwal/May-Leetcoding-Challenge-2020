#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
#Examples:
#
#s = "leetcode"
#return 0.
#
#s = "loveleetcode",
#return 2.
#Note: You may assume the string contain only lowercase letters.


class Solution(object):
    def firstUniqChar(self, s):
        
        d = {}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        ind = -1
        for i in s:
            ind+=1
            if d[i]==1:
                return ind
        return -1
