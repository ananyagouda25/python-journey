## Program: Finds the greatest common divisor of the greatest and smallest numbers in an array.
## Time complexity: O(n log n)
## Space complexity: O(n)


class Solution:
    def findGCD(self, nums: list[int]) -> int:
       sorty=sorted(nums)
       small=sorty.pop(0)  # Else use min(nums)
       large=sorty.pop()   # Else use max(nums)
       for i in range(1,small+1):
            if small%i==0 and large%i==0:
                gcd=i
       return gcd
sol=Solution()
print(sol.findGCD([2,5,6,9,10]))
