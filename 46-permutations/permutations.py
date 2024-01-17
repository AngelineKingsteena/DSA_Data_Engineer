class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i,subset):
            if i==len(nums):
                res.append(subset.copy())
                return
            for num in nums:
                if num not in subset:
                    backtrack(i+1,subset+[num])
        backtrack(0,[])
        return res