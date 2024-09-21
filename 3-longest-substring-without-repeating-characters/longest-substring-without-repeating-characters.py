class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         # def lengthOfLongestSubstring(s: str) -> int:
#         i, j = 0, 0  # Two pointers for the sliding window
#         N = len(s)  # Length of the string
#         cnt = {}  # Dictionary to count occurrences of characters
#         dup = 0  # To track the number of duplicate characters

#         while j < N:
#             # Increment the count of the current character
#             cnt[s[j]] = cnt.get(s[j], 0) + 1
#             # Increment duplicates if this character count becomes 2
#             if cnt[s[j]] == 2:
#                 dup += 1
            
#             # If there are duplicates, increment i to shrink the window
#             if dup > 0:
#                 if cnt[s[i]] == 2:
#                     dup -= 1
#                 cnt[s[i]] -= 1
#                 i += 1
            
#             j += 1  # Move the right pointer to expand the window

#         return j - i  # Return the length of the longest substring

# # s = "abcabcbb"
# # print(lengthOfLongestSubstring(s))  # Output: 3

        i, j = 0, 0  # Two pointers for the sliding window
        N = len(s)  # Length of the string
        ans = 0  # To store the length of the longest substring
        cnt = {}  # Dictionary to count the occurrences of characters

        # Iterate through the string with the right pointer (j)
        while j < N:
            # Update the count of the current character in the dictionary
            cnt[s[j]] = cnt.get(s[j], 0) + 1

            # If the current character has appeared more than once, move the left pointer (i)
            while cnt[s[j]] > 1:
                cnt[s[i]] -= 1
                i += 1  # Shrink the window from the left

            # Update the answer with the maximum length of the current valid window
            ans = max(ans, j - i + 1)

            # Move the right pointer (j) to expand the window
            j += 1

        return ans
