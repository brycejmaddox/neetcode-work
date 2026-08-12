# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root) -> int:
        if not root:
            return 0

        leftDepth = self.height(root.left)
        rightDepth = self.height(root.right)

        if rightDepth == -1 or leftDepth == -1:
            return -1

        if abs(leftDepth - rightDepth) > 1:
            return -1 
        return max(leftDepth, rightDepth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.height(root) != -1
        



        