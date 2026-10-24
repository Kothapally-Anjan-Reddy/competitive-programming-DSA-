"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        current_old=head
        head2=Node(head.val)
        current_new=head2
        nodes={None:None,current_old:current_new}

        while current_old.next:
            current_new.next=Node(current_old.next.val)
            current_old=current_old.next
            current_new=current_new.next
            nodes[current_old]=current_new
        
        current_new=head2
        current_old=head

        while current_new:
            current_new.random=nodes[current_old.random]
            current_old=current_old.next
            current_new=current_new.next

        return head2
