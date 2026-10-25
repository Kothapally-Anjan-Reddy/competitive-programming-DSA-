# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def listReverse(head):
    #Write your code here...
    current=head
    pre=None
    
    while(head.next!=None):
        head=head.next
        current.next=pre
        pre=current
        current=head
    
    head.next=pre
    
    return head
