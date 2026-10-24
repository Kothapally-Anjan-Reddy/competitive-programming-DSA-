# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode()
        h=l3
        quo=0
        while l1 and l2:
            new_node=ListNode()
            new_node.val=(l1.val+l2.val+quo)%10
            quo=(l1.val+l2.val+quo)//10
            h.next=new_node
            h=h.next
            l1=l1.next
            l2=l2.next
        while l1:
            new_node=ListNode()
            new_node.val=(l1.val+quo)%10
            quo=(l1.val+quo)//10
            h.next=new_node
            h=h.next
            l1=l1.next
            
        while l2:
            new_node=ListNode()
            new_node.val=(l2.val+quo)%10
            quo=(l2.val+quo)//10
            h.next=new_node
            h=h.next
            l2=l2.next
        
        if quo!=0:
            new_node=ListNode()
            new_node.val=quo
            h.next=new_node

        return l3.next
