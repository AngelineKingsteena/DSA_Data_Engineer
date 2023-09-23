class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for num in nums:
                # without if
                # Output
                # [[1,2,3],[1,3,3],[2,2,3],[2,3,3],[3,2,3],[3,3,3]]
                # Expected
                # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
                if num not in subset:
                    subset.append(num)
                    backtrack(subset)
                    subset.pop()
        backtrack([])
        return res

    



















                
        