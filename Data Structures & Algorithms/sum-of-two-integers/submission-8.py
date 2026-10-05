class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF # hexadecimal 32 bit from constains a and b are -1000 to 1000 it wil fix comfortably in 32 bit lol
        while b != 0:
            carry = (b & a ) << 1
            a = (a ^ b) & mask
            b =  carry & mask

        return a if a <= 0x7FFFFFFF else ~(a ^ mask) # we are doing that for negative numbers because we need to extent it with leading 1s infinit based on python precision 
