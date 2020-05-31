#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
#Example 1:
#Input: [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#Example 2:
#Input: [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#Note: The length of the given binary array will not exceed 50,000.
#


class Solution(object):
    def findMaxLength(self, nums):
        max_len = 0
        balance = 0         # net 1s - 0s
        balances = {0: -1}  # key is balance, value is index

        for i, num in enumerate(nums):

            if num == 1:
                balance += 1
            else:
                balance -= 1

            if balance in balances:
                max_len = max(max_len, i - balances[balance])
            else:
                balances[balance] = i

        return max_len