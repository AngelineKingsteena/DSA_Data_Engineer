# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## https://docs.google.com/document/d/1l9UDlLZeP0mQxExqjepsKbgYQj4nrNGUsyDlKDA1jyg/edit?usp=sharing
        head = ListNode()
        ans = head
        carry = 0
        while(l1 or l2 or carry):
            
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            c = a + b + carry
            carry = 1 if c >= 10 else 0
            digit = c % 10
            
            ans.next = ListNode(digit) ## notice ans.next and not just ans =,this is to connect head to ans,in 1st iteration
            
            ans = ans.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            
        return head.next
            

# while calculating carry, we know that largesr one digit number is 9 so 9 + 9 = 18 and if there is any carry then + 1 = 19 will be the largest sum that we will get. So carry will always be one and not more that one.

        
