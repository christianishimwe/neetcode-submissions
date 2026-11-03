# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- go to the left and check if it is a valid binary search tree
- actually, check from this node it it is a valid binary serach tree
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # check the value on the left and the value on the right
        # we need to keep track of the min and the max
        # (max, min, valid)
        def valid(node, left, right):
            if not node:
                return True
            if node.val <= left:
                return False
            if node.val >= right:
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float('-inf'), float('inf'))