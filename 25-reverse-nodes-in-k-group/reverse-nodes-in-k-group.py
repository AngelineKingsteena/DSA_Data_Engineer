# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # https://docs.google.com/document/d/1l9UDlLZeP0mQxExqjepsKbgYQj4nrNGUsyDlKDA1jyg/edit#heading=h.a7d3sil9l2qs
#         Let's reverse 1 -> 2 -> 3 (k = 2).
# Before we start reversing, append dummy head first: dummy -> 1 -> 2 -> 3.
# Instead of explaning with text, let me show visual flow of my code.
# cnt = 0
# head
# dummy -> 1   -> 2 -> 3
# prev     cur

# cnt = 1
# head
# dummy <-> 1     2 -> 3
#           prev  cur

# cnt = 2
# head
# dummy <-> 1  <- 2    3
#                 prev cur

# cnt % k == 0, update head.
#          head
#           ┌----------↓
# dummy     1  <- 2    3
#           prev       cur
#    └------------↑

# Finally, first k nodes are reversed.
#              head
# dummy -> 2 -> 1    -> 3
#               prev    cur

# cnt = 3
#              head
# dummy -> 2 -> 1   <-> 3      (nil)
#                       prev    cur

# Now, cur is nil, but cnt % k is not 0. We have to revert remaining nodes with substracting cnt by 1 until cnt % 2 becomes 0.
# cnt = 2
#              head
# dummy -> 2 -> 1    -> 3
#               prev    cur

# Done.

        root = ListNode(next=head) # dummy
        prev = head = root
        cur = head.next
        cnt = 0

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
            cnt += 1

            if cnt % k == 0:
                head.next.next, head.next, head = cur, prev, head.next
                prev = head

        while cnt % k:
            prev.next, prev, cur = cur, prev.next, prev
            cnt -= 1

        return root.next

        