# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # def dfs(root):
        #     if root.left:
        #         if root.left.val>=root.val:
        #             return False
        #         res=dfs(root.left)
        #         if res==False: return False
            
        #     if root.right:
        #         if root.right.val<=root.val:
        #             return False
        #         res=dfs(root.right)
        #         if res==False: return False

        #     return True
        
        # res=dfs(root)
        # return res

        nodes=[]

        def inorder(root):
            if root.left:
                inorder(root.left)
                
            nodes.append(root.val)

            if root.right:
                inorder(root.right)

        inorder(root)

        for i,value in enumerate(nodes):
            if i>0 and nodes[i]<=nodes[i-1]:
                return False
        
        return True
