
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        q=[]
        counter=itertools.count()
        for node in lists:
            if node:
                q.append((node.val,next(counter),node))
        heapq.heapify(q)
        head=ListNode()
        curr=head

        while q:
            val,itr,node=heapq.heappop(q)
            curr.next=ListNode(val)
            curr=curr.next
            if node.next:
                node=node.next
                heapq.heappush(q,(node.val,next(counter),node))
        
        return head.next
