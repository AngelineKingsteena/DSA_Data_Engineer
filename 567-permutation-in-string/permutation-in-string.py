class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        table = defaultdict(int)

        for c in s1:
            table[c] += 1

        begin, end = 0, 0
        counter = len(table)

        while end < len(s2):
            endchar = s2[end]

            if endchar in table:
                table[endchar] -= 1
                if table[endchar] == 0:
                    counter -= 1

            end += 1

            while counter == 0:
                if end - begin == len(s1):
                    return True

                startchar = s2[begin]

                if startchar in table:
                    table[startchar] += 1
                    if table[startchar] > 0:
                        counter += 1

                begin += 1

        return False
