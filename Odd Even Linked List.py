#Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
#You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
#Example 1:
#
#Input: 1->2->3->4->5->NULL
#Output: 1->3->5->2->4->NULL
#Example 2:
#
#Input: 2->1->3->5->6->4->7->NULL
#Output: 2->3->6->7->1->5->4->NULL
#Note:
#
#The relative order inside both the even and odd groups should remain as it was in the input.
#The first node is considered odd, the second node even and so on ...

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even_head = even = ListNode(None)
        odd_head = odd = ListNode(None)
        
        while head:
            odd.next = head
            odd = odd.next
            
            even.next = head.next
            even = even.next
            
            head = head.next.next if even else None
        
        odd.next = even_head.next
        return odd_head.next