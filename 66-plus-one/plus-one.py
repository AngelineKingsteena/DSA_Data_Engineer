# Hard-Working Version: Manual Digit Check
# O(1) space, and O(1) time for most cases as well (with few chained 9's in the lower digits)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits
        i = len(digits)-1
        digits[i] += 1
        while digits[i]==10:
            digits[i] = 0
            if i==0:
                digits.insert(0,1)
            else:
                digits[i-1] += 1
                i -= 1
        return digits