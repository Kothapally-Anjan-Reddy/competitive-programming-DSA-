# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def counts(self,root:TreeNode,h:int)->int:
        if not root:
            return 0
        curr=root.val
        h=max(curr,h)
        l=self.counts(root.left,h)
        r=self.counts(root.right,h)
        if root.val>=h:
            return l+r+1
        return l+r

    def goodNodes(self, root: TreeNode) -> int:
        res=self.counts(root,root.val)
        return res
