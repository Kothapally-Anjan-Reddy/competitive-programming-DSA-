# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        fast=head.next.next
        slow=head.next

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        reverse=slow.next
        slow.next=None      #Make 1st list end point to null
        current=reverse
        prev=None

        while current.next:
            reverse=current.next
            current.next=prev
            prev=current
            current=reverse
        current.next=prev

        reverse=current
        final=head
        current=head

        while current.next and reverse:
            final=final.next
            current.next=reverse
            current=current.next
            reverse=reverse.next
            current.next=final
            current=current.next
        """
        Do not return anything, modify head in-place instead.
        """
