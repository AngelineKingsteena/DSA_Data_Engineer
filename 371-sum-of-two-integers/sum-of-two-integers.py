class Solution:
    ## RC ##
        ## APPROACH : BITWISE OPERATIONS ##
        ## LOGIC ##
        # if you notice 1+1=0 with carry 1,1+0=1(so excluding
        # carry its similar to xor functioning)
        # and carry= left-shifted and-ed result
    #     EXAMPLE:-addition of 9 and 11
    #     carry   =   11
    #     a(9)    =  1001
    #     b(11)   =  1011
    #     a+b     = 10100 
    #    ======================
    #     PROGRAM RUNS LIKE
    #     a(9)    =  1001
    #     b(11)   =  1011
    #      -----------------
    #     a^b     =  0010
    #     a&b<<1  = 10010  (carry)
    #      -----------------
    #     a^b     = 10000
    #     a&b<<1  = 00100  (carry)
    #      -----------------
    #     a^b     = 10100
    #     a&b<<1  = 00000  (carry) 

		## TIME COMPLEXITY : O(1) ##
		## SPACE COMPLEXITY : O(1) ##
        
        # 32 bit mask in hexadecimal
         # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while(b & mask > 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a