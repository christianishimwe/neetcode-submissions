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
        left_val, right_val, result = self.helper(root)
        return result

    def helper(self, root):
        if not root:
            return (float('-inf'), float('inf'), True)
        # from left
        max_left, min_left, valid_left = self.helper(root.left)
        if not valid_left:
            return (float('-inf'), float('inf'), False)
        max_right, min_right, valid_right = self.helper(root.right)
        if not valid_right:
            return (float('-inf'), float('inf'), False)
        # now do the check here too
        if max_left >= root.val:
            return (float('-inf'), float('inf'), False)
        if min_right <= root.val:
            return (float('-inf'), float('inf'), False)
        max_root = max(max_left, max_right, root.val)
        min_root = min(min_left, min_right, root.val)
        return (max_root, min_root, True)


        