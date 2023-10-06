class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=nIVW4P8b1VA&ab_channel=NeetCode
        left, right = 0, len(nums) - 1
    
        while left <= right:
            if nums[left] <= nums[right]:
                # If the leftmost element is less than or equal to the rightmost element,
                # it means the array is already sorted, and the minimum is at the 'left' index.
                return nums[left]

            mid =( left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # The minimum element will be at the 'left' index
        return nums[left]
                