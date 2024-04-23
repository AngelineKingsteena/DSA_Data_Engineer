class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        def helper(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l,r=l+1,r-1
        i,j=0,len(nums)-1
        helper(i,j)
        i,j=0,k-1
        helper(i,j)
        i,j=k,len(nums)-1
        helper(i,j)


# let's do a dry run with an example list 
# nums = [1, 2, 3, 4, 5, 6, 7] and k = 3:
# k=k%len(nums): 
# k = 3 % 7 = 3
# helper(i,j): 
# Reverse the entire list: nums = [7, 6, 5, 4, 3, 2, 1]
# i,j=0,k-1 and helper(i,j): 
# Reverse the first k elements: nums = [5, 6, 7, 4, 3, 2, 1]
# i,j=k,len(nums)-1 and helper(i,j): 
# Reverse the remaining elements: nums = [5, 6, 7, 1, 2, 3, 4]
