# Prgogram: Checks if a given number is a happy number or not.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.

# Time complexity: O(log n)
# Space complexity: O(log n) using the total set.


class Solution:
    def isHappy(self, n: int) -> bool:
        total=set()
        while True:
            sqsum=0
            while n>0:
                i=n%10
                n//=10
                sqsum+=i**2
            if sqsum==1:
                return True
            n=sqsum
            if sqsum in total:
                return False
            total.add(sqsum)
sol=Solution()
print(sol.isHappy(19))
        
