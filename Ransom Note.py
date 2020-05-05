#Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
#Each letter in the magazine string can only be used once in your ransom note.
#
#Note:
#You may assume that both strings contain only lowercase letters.
#
#canConstruct("a", "b") -> false
#canConstruct("aa", "ab") -> false
#canConstruct("aa", "aab") -> true



class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        from collections import Counter
        
        ran_C = Counter(ransomNote)
        mag_C = Counter(magazine)
        
        for i in ran_C:
            if i not in mag_C or mag_C[i] < ran_C[i]:
                return False
        
        return True