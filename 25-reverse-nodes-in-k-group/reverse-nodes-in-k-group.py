# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        #The first for loop runs for k iterations. Its purpose is to check if there are at least k nodes remaining in the list. If not, it returns the original head, as reversing is not possible.
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        	
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head

        # Once the first group of k nodes is reversed, the prev variable points to the new head of the reversed group,`head` is the tail of the group and the curr variable points to the next group of nodes that haven't been processed yet.

        for _ in range(k): ## instead of while curr: cause,we need to reverse only k-group,not entire linke list
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        
        # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr, k)
        return prev
