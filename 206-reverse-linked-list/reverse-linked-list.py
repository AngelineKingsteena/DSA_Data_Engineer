# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## video solution :-https://www.youtube.com/watch?v=G0_I-ZF0S38&ab_channel=NeetCode
        prev, curr = None, head
        # T O(n) M 0(1)
        while curr:
            # nxt = curr.next
            # curr.next = prev
            # prev = curr
            # curr = nxt
            curr.next, prev, curr = prev, curr, curr.next
        return prev
        
# BEFORE(ACCORDING TO 1-->2-->NONE)
# C-1,P-NONE,N-2

# AFTER(ACCORDING TO NONE<--1<--2)
# C-2,P-1,N-NONE