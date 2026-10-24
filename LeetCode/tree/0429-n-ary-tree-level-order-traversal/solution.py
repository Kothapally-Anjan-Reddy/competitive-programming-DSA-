"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        results=[]
        queue=collections.deque([root])

        while queue:
            level_items=[]
            for _ in range(0,len(queue)):
                
                node=queue.popleft()
                level_items.append(node.val)
                if node.children:
                    queue.extend(node.children)

            results.append(level_items)

        return results
