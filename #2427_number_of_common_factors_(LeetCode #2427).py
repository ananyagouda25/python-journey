# Program: Number of common factors
# Time complexity: O(min(a, b))
# Space complexity: O(min(a, b))

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        for i in range(1,min(a,b)+1):
            if (a%i==0 and b%i==0):
                count+=1
        return count
cal= Solution()
print(cal.commonFactors(12,6))
