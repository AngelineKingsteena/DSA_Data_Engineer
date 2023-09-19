# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## video solution :-https://www.youtube.com/watch?v=XVuQxVej6y8&ab_channel=NeetCode

        ## idea:-
        # use 2 pointers,where right is 1st offset from left by n
        # and later both left and the offsetted right pointers 
        # keep moving 1step until right becomes null.
        # with dummy node at start,and the 
        #  movement cause by above l,r pointers ,
        # left will be exactly at node 3 (in eg 1 pic)
    
        dummy = ListNode (0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left. next
            right = right. next
        # delete
        left.next = left.next. next
        return dummy. next
        