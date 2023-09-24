class Solution:
	def longestPalindrome(self, s: str) -> str:
		# it starts searching for a palindrome from a single character position. It essentially treats the character at index as the center of a potential odd-length palindrome.

# 		when helper(index, index) is called, it starts expanding from the single character at position index as the potential center of an odd-length palindrome.

# Similarly, when helper(index, index + 1) is called, it starts expanding from the two adjacent characters at positions index and index + 1 as the potential center of an even-length palindrome.
		res = ""
		def helper(left: int, right: int):
			while left >= 0 and right <len(s) and s[left]==s[right]:
				left -= 1
				right += 1				
			return s[left + 1 : right]
		for index in range(len(s)):
			###max(odd,even,res)
			###key=len says use len function on output/arguments
			res = max(helper(index, index), helper(index, index + 1), res, key = len)
		return res
        