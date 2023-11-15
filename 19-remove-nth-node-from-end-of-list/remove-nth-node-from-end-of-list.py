# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## video solution :-https://www.youtube.com/watch?v=XVuQxVej6y8&ab_channel=NeetCode

        ## idea:-
        # use 2 pointers,where fast is 1st offset from slow by n
        # and later both slow and the offsetted fast pointers 
        # keep moving 1step until fast becomes null.
        # with dummy node at start,and the 
        #  movement cause by above fast,slow pointers ,
        # slow will be exactly at node 3 (in eg 1 pic)
    
        dummy=ListNode(0,head)
        slow=dummy
        fast=head
        while n>0 and fast:
            fast=fast.next
            n-=1
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next
        
