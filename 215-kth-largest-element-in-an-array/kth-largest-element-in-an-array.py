# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # idea :- kth largest element is the first element in minheap of size k
        n=nums
        heapq. heapify (n)
        while len(n) > k:
            heapq.heappop(n)
        return n[0]
