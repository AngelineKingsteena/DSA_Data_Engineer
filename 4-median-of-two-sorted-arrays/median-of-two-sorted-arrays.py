class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## video solution :-https://www.youtube.com/watch?v=q6IEA26hvXc&ab_channel=NeetCode
        A, B = nums1, nums2
        total = len(nums1) + len (nums2)
        # when we partition,we want our left partition to be roughly = half
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A # uptil i is left partition of a
            ##-2 BCOZ HALF-I WILL CONSIDER INDICES,BUT WE WANT HALF OF NO. OF ELEMENTS RATHER THAN INDICES,2 BECOZ J STARTS AT 0,I STARTS AT 0
            j= half - i - 2 # B # uptil j is left partition of b
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
            # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # This is because the current partition is too far to the right in A, so we reduce r to bring i to the left.
                # eg:a4 left,b3right
                r = i-1
            elif Bleft > Aright:
                l= i +1

#### BELOW IS FOR WHILE L<=R
                
        # A, B = nums1, nums2
        # total = len(nums1) + len(nums2)
        # half = total // 2

        # if len(B) < len(A):
        #     A, B = B, A

        # l, r = 0, len(A) - 1

        # while l <= r:
        #     i = (l + r) // 2
        #     j = half - i - 2
        #     Aleft = A[i] if i >= 0 else float("-infinity")
        #     Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        #     Bleft = B[j] if j >= 0 else float("-infinity")
        #     Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        #     if Aleft <= Bright and Bleft <= Aright:
        #         if total % 2:
        #             return min(Aright, Bright)
        #         return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        #     elif Aleft > Bright:
        #         r = i - 1
        #     else:
        #         l = i + 1

        # # If the loop completes without returning, it means the arrays are not sorted.
        # # Handle this case by returning the median using the last known indices.
        # i = (l + r) // 2
        # j = half - i - 2
        # Aleft = A[i] if i >= 0 else float("-infinity")
        # Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        # Bleft = B[j] if j >= 0 else float("-infinity")
        # Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # if total % 2:
        #     return min(Aright, Bright)
        # return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
