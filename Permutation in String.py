#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
#
# 
#
#Example 1:
#
#Input: s1 = "ab" s2 = "eidbaooo"
#Output: True
#Explanation: s2 contains one permutation of s1 ("ba").
#Example 2:
#
#Input:s1= "ab" s2 = "eidboaoo"
#Output: False
# 
#
#Note:
#
#The input strings only contain lower case letters.
#The length of both given strings is in range [1, 10,000].

class Solution(object):
    def checkInclusion(self, s1, s2):
        n1 = len(s1)
        freq = [0] * 26     # counts of each char

        for c in s1:
            freq[ord(c) - ord("a")] += 1

        for i, c in enumerate(s2):

            freq[ord(c) - ord("a")] -= 1    # decrement count of letter added to window
            if i >= n1:
                freq[ord(s2[i - n1]) - ord("a")] += 1   # increment count of letter exiting window

            if not any(freq):
                return True

        return False 