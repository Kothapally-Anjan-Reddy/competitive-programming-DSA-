# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        que=collections.deque([root])

        while que:
            level_items=[]
            for _ in range(0,len(que)):
                node=que.popleft()
                level_items.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                # if node.children:
                #     queue.extend(node.children)       ->This is only when there are many children and they are in a array.
            res.append(level_items)
        return res
