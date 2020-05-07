#In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
#Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
#We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
#Return true if and only if the nodes corresponding to the values x and y are cousins.
#
# 
#
#Example 1:
#
#
#Input: root = [1,2,3,4], x = 4, y = 3
#Output: false
#Example 2:
#
#
#Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
#Output: true
#Example 3:
#
#
#
#Input: root = [1,2,3,null,4], x = 2, y = 3
#Output: false


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        val_to_node = {root.val: root}  # value to nodes at current depth
        node_to_parent = {root: None}

        while True:

            x_node = val_to_node.get(x, None)
            y_node = val_to_node.get(y, None)
            if x_node is not None and y_node is not None:
                return node_to_parent[x_node] != node_to_parent[y_node]
            if x_node is not None or y_node is not None:
                return False

            new_val_to_node = {}
            for node in val_to_node.values():
                if node.left:
                    node_to_parent[node.left] = node
                    new_val_to_node[node.left.val] = node.left
                if node.right:
                    node_to_parent[node.right] = node
                    new_val_to_node[node.right.val] = node.right
            val_to_node = new_val_to_node