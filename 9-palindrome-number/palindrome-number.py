class Solution:
    def isPalindrome(self, x: int) -> bool:  
        # If x is negative or ends with 0 (but is not 0), it's not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # To store the reversed half of x
        reversed_x = 0
        # Reverse the second half of x and compare with the first half
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        # When the length is an odd number, we can get rid of the middle digit by reversed_x//10
        # For example, when dealing with 12321, at the end of the loop we get x = 12, reversed_x = 123,
        # since the middle digit doesn't matter in palindrome (it will always equal to itself), we can simply get rid of it.
        return x == reversed_x or x == reversed_x // 10