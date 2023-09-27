class Solution:
    # https://leetcode.com/problems/interleaving-string/solutions/3956393/99-78-2-approaches-dp-recursion/
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        #If m < n, swap s1 and s2. This is to ensure that s1 is not longer than s2, which helps in optimizing the space complexity to O(min(m, n))
        if m < n:
            return self.isInterleave(s2, s1, s3)
        dp = [False] * (n + 1)
        # dp[0] = True because you can always form an empty string from empty strings.
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n + 1):
                #For each character in s1, iterate through s2 and update the dp array based on the transition rule: dp[j] = (dp[j] and s1[i] == s3[i+j]) or (dp[j-1] and s2[j] == s3[i+j]).
# The transition rule checks if the current s3[i+j] can be matched by either s1[i] or s2[j], relying solely on the previous values in the dp array.
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[n]