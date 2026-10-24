# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        total=0
        current=head

        while current:
            total+=1
            current=current.next
        
        if total==n:
            head=head.next
            return head

        pos=total-n
        current=head
        while pos>1:
            current=current.next
            pos-=1
        current.next=current.next.next

        return head
