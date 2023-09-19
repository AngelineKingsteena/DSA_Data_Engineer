class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode

        ### idea 
        # in eg 1:- [1,3,4,2,2] if 3& 4 are considered as indices
        #  both values at 3rd and 4th indice refer to same no. 2
        #  which implies a cycle
       
        ### this loop is just to make slow and fast to meet
        slow, fast = 0,0
        while True:
            slow = nums [slow] ## implies fast is moving 1 pointer ahed
            fast = nums [nums [fast]] ## implies fast is moving 2 pointers ahead
            if slow == fast:
                break
        ## incase of [1,2,3,1] the first node where above adjusted slow 
        ## and new slow2 meet is the repeating number,which is 1
        slow2 = 0
        while True:
            slow = nums [slow]
            slow2 = nums [slow2]
            if slow == slow2:
                return slow
        