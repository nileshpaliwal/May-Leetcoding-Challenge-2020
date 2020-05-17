#Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
#Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
#The order of output does not matter.
#
#Example 1:
#
#Input:
#s: "cbaebabacd" p: "abc"
#
#Output:
#[0, 6]
#
#Explanation:
#The substring with start index = 0 is "cba", which is an anagram of "abc".
#The substring with start index = 6 is "bac", which is an anagram of "abc".
#Example 2:
#
#Input:
#s: "abab" p: "ab"
#
#Output:
#[0, 1, 2]
#
#Explanation:
#The substring with start index = 0 is "ab", which is an anagram of "ab".
#The substring with start index = 1 is "ba", which is an anagram of "ab".
#The substring with start index = 2 is "ab", which is an anagram of "ab".

from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        freq = defaultdict(int)     # map from char to net count of char in sliding window
        result = []

        if n > len(s):              # no anagrams are possible
            return result

        def update_freq(c, step):   # updates dictionary and deletes zero values
            freq[c] += step
            if freq[c] == 0:
                del freq[c]

        for c1, c2 in zip(p, s[:n]):    # populate initial window
            update_freq(c1, -1)
            update_freq(c2, 1)

        for i in range(len(s) - n):
            if not freq:
                result.append(i)
            update_freq(s[i], -1)       # remove char at back of window
            update_freq(s[i + n], 1)    # add char at front of window

        if not freq:
            result.append(len(s) - n)
        return result