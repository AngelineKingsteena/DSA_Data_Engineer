# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ## video solution :- https://www.youtube.com/watch?v=RCuBc4Zl-oY&ab_channel=TimothyHChang


        h = []
        for i,l in enumerate(lists):
            if l: heappush(h, (l.val, i))
        dummy = curr = ListNode(0)
        while h:
            val, i = heappop(h)
            curr.next = ListNode(val)
            if lists[i].next:
                heappush(h, (lists[i].next.val, i))
                lists[i] = lists[i].next
            curr = curr.next
        return dummy .next
                