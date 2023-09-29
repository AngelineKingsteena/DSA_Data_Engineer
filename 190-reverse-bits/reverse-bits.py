class Solution:
    def reverseBits(self, n: int) -> int:
        # https://www.youtube.com/watch?v=UcoN6UjAI64&ab_channel=NeetCode
        res=0
        for i in range (32):
            # take each bit from right
            bit = (n >> i) & 1
            # add it to extreme left bit in total 32 bit
            res = res | (bit << (31 - i))
        return res