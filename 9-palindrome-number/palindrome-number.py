class Solution:
    def isPalindrome(self, n: int) -> bool:  
        # If x is negative or ends with 0 (but is not 0), it's not a palindrome
        if n < 0 or (n % 10 == 0 and n != 0):
            return False
        reversed_x=0
        x=n
        while x!=0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return n == reversed_x 