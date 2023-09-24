class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for w in wordDict:
                if i - len(w) >= 0 and dp[i - len(w)] and s[:i].endswith(w):
                    dp[i] = True
                    break
        return dp[-1]

# This is based on Python. Other might be different a bit.

# Initialize a list dp of size len(s) + 1, where dp[i] will indicate whether the substring up to index i (inclusive) can be segmented into words from wordDict. Initialize dp[0] as True, since an empty string can always be segmented.

# Iterate over each index i from 1 to len(s) + 1 (outer loop):

# For each index i,iterate over each word w in wordDict (inner loop):
# Check if the current word w can be appended to the substring ending at index i - len(w).
# This is done by verifying three conditions:
# i - len(w) >= 0: This ensures that the current word can be fit within the current index i.
# dp[i - len(w)]: This checks if the substring before the current word can be segmented into words from wordDict.
# s[:i].endswith(w): This checks if the current substring ending at index i ends with the word w.
# If all three conditions are satisfied, it means that the substring up to index i can be segmented using words from wordDict. In this case, set dp[i] to True.

# After iterating through all words in wordDict and updating dp[i] for the current index i, move on to the next index in the outer loop.

# Continue this process until you've iterated over all possible indices i from 1 to len(s).

# Finally, return dp[-1], which indicates whether the entire string s can be segmented using words from wordDict.

# In essence, the algorithm uses dynamic programming to build up the dp array, where each entry represents whether a certain substring can be segmented using the words from the dictionary. The algorithm leverages the fact that if a substring up to index i can be segmented, and a word from wordDict can be appended to it to reach index i, then the substring up to index i + len(word) can also be segmented.

# Complexity
# Time complexity: O(n * m * k)
# n is length of input string and m is length of wordDict. nested loop is n * m and in the nested loop. We check substring operations which costs O(k).

# Space complexity: O(n)
# For dp list. n is the length of the string s