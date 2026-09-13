# Program: It calculates the square root of a number without using the existing mathematical functions.
# Concepts: Binary search
# Time: O(log x) | Space: O(1)

class Solution:
    def mySqrt(self,x:int)-> int:
        low=0
        high=x
        while low<=high:
            mid=(low+high)//2
            if (mid*mid)==x:
                return mid
            elif (mid*mid)<x:
                low=mid+1
            else:
                high=mid-1
        return high
sol=Solution()
a=int(input())
print(sol.mySqrt(a))
