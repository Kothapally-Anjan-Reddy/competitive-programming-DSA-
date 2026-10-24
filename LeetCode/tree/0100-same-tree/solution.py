# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p)!=(not q):
            return False
        if p:
            if p.val!=q.val:
                return False
            l=self.isSameTree(p.left,q.left)
            if l==False:
                return False
            r=self.isSameTree(p.right,q.right)
            if r==False:
                return False
        return True
