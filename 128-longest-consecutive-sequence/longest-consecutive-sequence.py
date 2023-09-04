class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # video explanation--https://www.youtube.com/watch?v=P6RZZMu_maU&ab_channel=NeetCode
        numSet = set(nums)
        longest = 0
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
                