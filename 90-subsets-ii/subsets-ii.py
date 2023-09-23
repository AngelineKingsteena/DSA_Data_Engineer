class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, tmp):
            ans.append(tmp[:])
            for i in range(start, len(nums)):
                # Skip duplicates to avoid duplicate subsets
                if i > start and nums[i] == nums[i - 1]:
                    continue
                tmp.append(nums[i])
                backtrack(i + 1, tmp)
                tmp.pop()
        
        ans = []
        nums.sort()  # Sort the input list to handle duplicates
        backtrack(0, [])
        return ans
