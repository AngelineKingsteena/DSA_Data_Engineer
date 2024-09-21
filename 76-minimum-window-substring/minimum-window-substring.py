from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        table = defaultdict(int)

        # Initialize frequency table for t
        for c in t:
            table[c] += 1

        # Initialize sliding window
        begin, end = 0, 0
        counter = len(table)
        len_min = float('inf')
        ans = ""

        # Start sliding window
        while end < len(s):
            endchar = s[end]

            # If current char found in table, decrement count
            if endchar in table:
                table[endchar] -= 1
                if table[endchar] == 0:
                    counter -= 1

            end += 1

            # If counter == 0, means we found an answer, now try to trim that window
            while counter == 0:
                # Store new answer if smaller than previously best
                if end - begin < len_min:
                    len_min = end - begin
                    ans = s[begin:end]

                # Try to shrink the window from the left
                startchar = s[begin]

                if startchar in table:
                    table[startchar] += 1
                    if table[startchar] > 0:
                        counter += 1

                begin += 1

        return ans
