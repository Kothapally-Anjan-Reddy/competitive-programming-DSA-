# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Method-1:Updated
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root


        ## Method-1
        # if p.val<=root.val and q.val<=root.val:
        #     if p.val==root.val or q.val==root.val:
        #         return root
        #     return self.lowestCommonAncestor(root.left,p,q)
        # elif p.val>=root.val and q.val>=root.val:
        #     if p.val==root.val or q.val==root.val:
        #         return root
        #     return self.lowestCommonAncestor(root.right,p,q)
        # else:
        #     return root

        ## Method-2
        #     while True:
        # if p.val<root.val and q.val<root.val:
        #     root=root.left
        # elif p.val>root.val and q.val>root.val:
        #     root=root.right
        # else:
        #     return root
