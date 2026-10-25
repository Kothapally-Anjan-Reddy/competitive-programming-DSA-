"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def getMiddleElement(head):
    fast=head
    slow=head
    
    while fast.next!=None:
        slow=slow.next
        if fast.next.next!=None:
            fast=fast.next.next
        else:
            fast=fast.next
    
    return slow.data
