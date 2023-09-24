class Solution:
    def hammingWeight(self, n: int) -> int:
        # https://www.youtube.com/watch?v=5Km3utixwZs&ab_channel=NeetCode
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
                