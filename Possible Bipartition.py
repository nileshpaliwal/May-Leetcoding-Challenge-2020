#Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
#Each person may dislike some other people, and they should not go into the same group. 
#
#Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
#Return true if and only if it is possible to split everyone into two groups in this way.
#
# 
#
#Example 1:
#
#Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
#Output: true
#Explanation: group1 [1,4], group2 [2,3]
#Example 2:
#
#Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
#Output: false
#Example 3:
#
#Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
#Output: false
# 
#
#Constraints:
#
#1 <= N <= 2000
#0 <= dislikes.length <= 10000
#dislikes[i].length == 2
#1 <= dislikes[i][j] <= N
#dislikes[i][0] < dislikes[i][1]
#There does not exist i != j for which dislikes[i] == dislikes[j].


from collections import defaultdict

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        dislike = defaultdict(set)          # map each person to the set of people they dislike
        for a, b in dislikes:
            dislike[a].add(b)
            dislike[b].add(a)

        this, other = set(), set()          # 2 groups of people

        for i in range(1, N + 1):

            if i in this or i in other:     # already placed this person in a group
                continue
            to_add = {i}

            while to_add:

                this |= to_add              # put to_add in this

                disliked = set()            # people disliked by the people in to_add
                for num in to_add:
                    disliked |= dislike[num]
                if disliked & this:         # somebody dislikes somebody else in this group
                    return False

                disliked -= other           # remove people already in other
                to_add = disliked
                this, other = other, this

        return True