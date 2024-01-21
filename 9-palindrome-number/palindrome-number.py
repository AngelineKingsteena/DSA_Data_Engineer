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
        print(reversed_x)
        # When the length is an odd number, we can get rid of the middle digit by reversed_x//10
        # For example, when dealing with 12321, at the end of the loop we get x = 12, reversed_x = 123,
        # since the middle digit doesn't matter in palindrome (it will always equal to itself), we can simply get rid of it.
        return n == reversed_x #or x == reversed_x // 10