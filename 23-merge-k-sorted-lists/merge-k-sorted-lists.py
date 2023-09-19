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
            if l: 
                # print("22 ",h)
                heappush(h, (l.val, i))
                
        dummy = curr = ListNode(0)
        # print("33 ",h)
        while h:
            # print("44 ",h)
            val, i = heappop(h)
            # print("55 ",h)
            curr.next = ListNode(val)
            # print(f"66 {lists[i]} i {i}")
            if lists[i].next:
                # print("77 ",h)
                heappush(h, (lists[i].next.val, i))
                # print("88 ",h)
                lists[i] = lists[i].next
                # print(f"99 {lists[i]} i {i}")
            curr = curr.next
        return dummy.next
                