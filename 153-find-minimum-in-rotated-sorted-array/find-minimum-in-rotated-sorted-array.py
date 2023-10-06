class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=nIVW4P8b1VA&ab_channel=NeetCode
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right )// 2
            
            # Check if the mid element is greater than the rightmost element
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        # The minimum element will be at the 'left' index
        return nums[left]
            