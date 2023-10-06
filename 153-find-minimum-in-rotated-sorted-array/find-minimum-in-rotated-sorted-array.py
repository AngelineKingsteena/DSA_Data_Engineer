class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # if already in proper ascending order,obviously the leftmost is the minimum
            if nums[l] <= nums[r]:
                return nums[l]
            mid = (l + r) // 2
            # Check if the minimum element is in the left or right sorted portion
            #  checks whether the subarray from l to m is sorted,then right might have min,cause
                # | /|      in [4,5,6,7,0,1,2] (right has the min)
                # |/ | / 
                #    |/
            if nums[l] <= nums[mid]:
                # Minimum is in the right sorted portion
                l = mid + 1
            # if not sorted,min might be on the other side i,.e right side
            else:
                # Minimum is in the left sorted portion
                r = mid  

# why r=mid instead of r=mid-1?
# If nums[mid] >= nums[l], setting r = mid - 1 would exclude the possibility of nums[mid] being the minimum element. This is because the minimum element is more likely to be in the right portion, and mid itself, could potentially be the minimum.
# r = mid allows the binary search to continue examining the rotated portion that contains mid as a potential minimum.  
