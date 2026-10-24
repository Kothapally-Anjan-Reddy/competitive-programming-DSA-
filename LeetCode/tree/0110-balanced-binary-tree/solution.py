# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]):
        if not root: return 0

        left=self.height(root.left)
        if left== -1: return -1
        
        right=self.height(root.right)
        if right== -1: return -1
        
        if abs(right-left)>1:
            return -1

        return max(right, left)+1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        elif not root.left and not root.right: return True
        else:
            var=self.height(root)
            return var!=-1
