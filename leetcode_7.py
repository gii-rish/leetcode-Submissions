'''return 0 if the reversed value goes outside the signed 32-bit integer range else return
the reversed number'''
class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[:0:-1].strip('0'))*-1 if x < 0 else int(str(x)[::-1])
        return 0 if result.bit_length()>31 else result 