# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # https://www.youtube.com/watch?v=gBTe7lFR3vc&ab_channel=NeetCode

        # idea floyd algor or tortoise and hare algo
        slow, fast = head, head ## fast would've been head.next,if ques was to find middle
        while fast and fast. next:
            slow = slow. next
            fast = fast.next. next
            if slow == fast:
                return True
        return False

        