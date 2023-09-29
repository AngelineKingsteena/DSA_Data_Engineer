class Solution:
    def hammingWeight(self, n: int) -> int:
        # https://www.youtube.com/watch?v=5Km3utixwZs&ab_channel=NeetCode
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
  
#   1st iteration
#         say n= 101
#           n-1= 100  
#    n &(n - 1)= 100 (basically we removed one count of 1)
#    ------------------------------------
#   2nd iteration
#         say n= 100
#           n-1= 011  
#    n &(n - 1)= 000 (now we removed another count of 1)
# so while will become 0 and break,we can return count
                