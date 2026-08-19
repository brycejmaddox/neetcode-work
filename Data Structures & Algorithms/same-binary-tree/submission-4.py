# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both p and q nodes are none, then they are the same
        if not p and not q:
            return True
        # If either p or q is None, then they aren't the same
        elif not p or not q:
            return False

        # Invoke recursion to run through the check for left and right children
        right = self.isSameTree(p.right,q.right)
        left = self.isSameTree(p.left,q.left)

        return right and left and p.val == q.val
