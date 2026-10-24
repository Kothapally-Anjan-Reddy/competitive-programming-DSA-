# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self,root):
        if not root: return 0
        
        left=self.recurse(root.left)
        right=self.recurse(root.right)
        return max(left+1,right+1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root: return 0
        # count=0
        # queue=collections.deque([root])

        # while queue:
        #     for _ in range(0,len(queue)):
        #         node=queue.popleft()

        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)
        #     count+=1

        # return count

        count=self.recurse(root)
        return count
