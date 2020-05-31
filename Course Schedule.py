#There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
#Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
#Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# 
#
#Example 1:
#
#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take. 
#             To take course 1 you should have finished course 0. So it is possible.
#Example 2:
#
#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false
#Explanation: There are a total of 2 courses to take. 
#             To take course 1 you should have finished course 0, and to take course 0 you should
#             also have finished course 1. So it is impossible.


from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nb_prerequisites = defaultdict(int)     # key is course, value is number of prerequisite courses
        prereq_list = defaultdict(list)         # key is a course, value is list of courses that depend on course

        for after, before in prerequisites:
            nb_prerequisites[after] += 1
            prereq_list[before].append(after)

        can_take = set(i for i in range(numCourses)) - set(nb_prerequisites.keys())

        while can_take:

            course = can_take.pop()                     # take any course with no prerequisites
            numCourses -= 1                             # decrement count of remaining courses to be taken
            for dependent in prereq_list[course]:
                nb_prerequisites[dependent] -= 1        # decrement count of dependencies
                if nb_prerequisites[dependent] == 0:    # no more prerequisites
                    can_take.add(dependent)

        return numCourses == 0