class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        def backtracking(res,visited,subset,nums):
            if len(subset) == len(nums):
                res.append(subset)
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtracking(res,visited,subset+[nums[i]],nums)
                    visited.remove(i)
        backtracking(res,visited,[],nums)
        return res

    



















                
        