# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root:Optional[TreeNode])->int:
        if not root:
            return [0,0]
        l=self.height(root.left)
        r=self.height(root.right)
        current=l[0]+r[0]
        h=max(current,l[1],r[1])
        return [max(l[0],r[0])+1,h]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=self.height(root)
        return res[1]
