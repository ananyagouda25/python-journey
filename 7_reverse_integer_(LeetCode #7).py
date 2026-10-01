# Program: Reverses the integer entered by user. Only accepts signed 32 bit integers.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0:1]=='-':
            rev=int(f"-{str(x)[:0:-1]}")
        elif x%10==0:
            x//=10
            rev=int(str(x)[::-1])
        else:
            rev=int(str(x)[::-1])
        if -(2**31) <= rev <= (2**31)-1:
            return rev
        else:
            return 0
sol=Solution()
print(sol.reverse(-123))
