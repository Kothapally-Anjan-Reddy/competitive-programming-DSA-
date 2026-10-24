# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root:Optional[TreeNode],targetSum:int) -> bool :
        if root.left:
            var=self.dfs(root.left,targetSum-root.left.val)
            if var: return True
            
        if root.right:
            var=self.dfs(root.right,targetSum-root.right.val)
            if var: return True
            
        if not root.left and not root.right:
            return targetSum==0

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root : return False
        
        var=self.dfs(root,targetSum-root.val)
        
        return var== True
