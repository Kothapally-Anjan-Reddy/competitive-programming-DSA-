"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if len(node.neighbors)==0:
            return Node(node.val)

        old_to_new={}
        visited=set()
        que=collections.deque()
        que.append(node)
        def cloningelements(node):
            while que:
                node=que.popleft()
                if not node: return
                if node not in visited:
                    copy=Node(node.val) # Here already neighbors is also added even value are not given
                    old_to_new[node]=copy
                    visited.add(node)
                    que.extend(node.neighbors)

        cloningelements(node)
        que.append(node)
        visited.clear()
        def cloningedges(node):
            while que:
                node=que.popleft()
                if not node: return
                if node not in visited:
                    visited.add(node)
                    # old_to_new[node].neighbors=[]      not required as statement above satifies it.
                    for i in node.neighbors:
                        old_to_new[node].neighbors.append(old_to_new[i])
                    que.extend(node.neighbors)
        
        cloningedges(node)

        return old_to_new[node]
