class Solution:
    def numDecodings(self, s: str) -> int:
        # https://leetcode.com/problems/decode-ways/solutions/1029225/simple-and-detail-solution-with-explanation/
        # cannot map to any character due to the leading zero
        if s[0] == '0':
            return 0
        n = len(s)
        # dp[i]: number of ways of decoding the substring s[:i]
        dp = [0 for _ in range(n + 1)]
        # base case
        dp[0] = 1
        for i in range(1, n + 1):
            # check single digit decode
            # valid deocde is possible only when s[i - 1] is not zero
            # if so, take the previous state dp[i - 1]
            # e.g. AB - 1[2]
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            # check double digit decode
            # by looking at the previous two digits
            # if the substring belongs to the range [10 - 26]
            # then add the previous state dp[i - 2]
            # e.g. L - [12]
            if i >= 2:
                # or you can use `stoi(s.substr(i - 2, 2))`
                x = int(s[i - 2: i])
                # check the range
                if 10 <= x <= 26:
                    dp[i] += dp[i - 2]
        return dp[n]
        