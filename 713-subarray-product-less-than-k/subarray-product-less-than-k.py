class Solution:
    def numSubarrayProductLessThanK(self, A: List[int], k: int) -> int:
        # def numSubarrayProductLessThanK(A, k):
        if k == 0:
            return 0
        
        i, j = 0, 0  # Two pointers for the sliding window
        N = len(A)  # Length of the array
        prod = 1  # Product of the current window
        ans = 0  # Count of valid subarrays

        for j in range(N):
            prod *= A[j]  # Update the product with the new right element
            
            # Shrink the window from the left until the product is less than k
            while i <= j and prod >= k:
                prod /= A[i]  # Remove the leftmost element from the product
                i += 1  # Move the left pointer to the right
            
            ans += j - i + 1  # Count all valid subarrays ending at j

        return ans

            