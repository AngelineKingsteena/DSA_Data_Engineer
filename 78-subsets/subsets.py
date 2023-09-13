class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## video solution :- https://www.youtube.com/watch?v=REOH22Xwdkk&ab_channel=NeetCode
        res = []
        subset = [ ]
        def dfs(i):
            if i >= len (nums):
                res.append(subset.copy ())
                return
            # decision to include nums [i]
            subset.append (nums [ i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset .pop ( )
            dfs(i + 1)
        dfs (0)
        return res
        