#Return the root node of a binary search tree that matches the given preorder traversal.
#
#(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
#
#It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.
#
#Example 1:
#
#Input: [8,5,1,7,10,12]
#Output: [8,5,10,1,7,null,12]
#
# 
#
#Constraints:
#
#1 <= preorder.length <= 100
#1 <= preorder[i] <= 10^8
#The values of preorder are distinct.


class Solution(object):
    def bstFromPreorder(self, preorder): 
        self.i = 0 
        

        def helper(max_value=float("inf")):
            if self.i >= len(preorder) or preorder[self.i] > max_value:
                return None

            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = helper(root.val)        # left subtree uses elements < root.val
            root.right = helper(max_value)      # right subtree uses elements < max_value
            return root

        return helper()