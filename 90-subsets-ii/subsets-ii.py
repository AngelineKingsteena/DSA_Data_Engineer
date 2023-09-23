class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # Sort the input list to handle duplicates
        nums.sort()  
        def backtrack(start, tmp):
            if start == len(nums):
                ans.append(tmp[:])
                return
            # Include the current element
            tmp.append(nums[start])
            backtrack(start + 1, tmp)
            tmp.pop()
            # Skip duplicates
            while start < len(nums) - 1 and nums[start] == nums[start + 1]:
                start += 1
            # Exclude the current element
            backtrack(start + 1, tmp)
        backtrack(0, [])
        return ans
