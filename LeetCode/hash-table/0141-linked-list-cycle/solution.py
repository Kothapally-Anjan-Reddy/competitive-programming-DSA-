# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            slow=head.next
            fast=head.next.next
            while fast and fast.next:
                if fast==slow:
                    return True
                fast=fast.next.next
                slow=slow.next
            
        return False
