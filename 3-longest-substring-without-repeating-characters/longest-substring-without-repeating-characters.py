class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # def lengthOfLongestSubstring(s: str) -> int:
        i, j = 0, 0  # Two pointers for the sliding window
        N = len(s)  # Length of the string
        cnt = {}  # Dictionary to count occurrences of characters
        dup = 0  # To track the number of duplicate characters

        while j < N:
            # Increment the count of the current character
            cnt[s[j]] = cnt.get(s[j], 0) + 1
            # Increment duplicates if this character count becomes 2
            if cnt[s[j]] == 2:
                dup += 1
            
            # If there are duplicates, increment i to shrink the window
            if dup > 0:
                if cnt[s[i]] == 2:
                    dup -= 1
                cnt[s[i]] -= 1
                i += 1
            
            j += 1  # Move the right pointer to expand the window

        return j - i  # Return the length of the longest substring

# s = "abcabcbb"
# print(lengthOfLongestSubstring(s))  # Output: 3

        