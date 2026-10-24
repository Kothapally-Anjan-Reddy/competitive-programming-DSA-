# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root)!=(not subRoot):
            return False
        if root:
            if root.val!=subRoot.val:
                return False
            l=self.check(root.left,subRoot.left)
            if l==False:
                return False
            r=self.check(root.right,subRoot.right)
            if r==False:
                return False
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root)!=(not subRoot):
            return False
        if root:
            if root.val==subRoot.val:
                res=self.check(root,subRoot)
                if res==True:
                    return True
            l=self.isSubtree(root.left,subRoot)
            if l==True:
                return True
            r=self.isSubtree(root.right,subRoot)
            if r==True:
                return True
        return False
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     res:Optional
    #     res=self.travel(root,subRoot)
    #     if res==True:return True
    #     else:return False
