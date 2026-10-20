## Program: Given an integer n, return true if it is a power of two. Otherwise, return false.
## Time complexity: O(1)
## Space complexity: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&(n-1))==0

# So bitwse AND operator: n&(n-1) 
# Ex: n=8.. n-1=7
#   8=1000 
# & 7=0111
#     0000.. So the resultant is 0 for numbers which are powers of 2/even..
# Ex: n=9.. n-1=8
#   9=1001
# & 8=1000
#     1000.. which is not equal to 0.. 
# The outer and operator is used to short circuit the whole step when input is negative..
