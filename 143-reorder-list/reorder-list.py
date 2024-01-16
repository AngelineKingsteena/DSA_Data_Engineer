# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ## video solution :-https://www.youtube.com/watch?v=S5bfdUTrKLM&ab_channel=NeetCode
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                break
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second. next = prev
            prev = second
            second = tmp
        
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second. next
            #reorder
            first.next = second
            second. next = tmp1
            #iterate
            first, second = tmp1, tmp2
                