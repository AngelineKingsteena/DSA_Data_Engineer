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
        while n>0 and fast:# notice no n>=0: cause it'll delete previous node to actual "to-be" deleted node
            ##cause :#and fast.next: will cause error in head =[1,2,3,4,5],n =2,Output=[1,2,4,5],Expected=[1,2,3,5]
            fast=fast.next
            n-=1
        while fast: :# notice no (and fast.next): cause it'll delete previous node to actual "to-be" deleted node
            ##cause :#and fast.next: will cause error in head =[1,2,3,4,5],n =2,Output=[1,2,4,5],Expected=[1,2,3,5]
            slow=slow.next
            fast=fast.next
            ## notice no need to break like linked list cycle
        slow.next=slow.next.next
        return dummy.next
        
