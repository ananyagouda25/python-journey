## Program: An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
## Given an integer n, returns true if n is an ugly number.
## Time complexity: O(log n)
## Space complexity: O(1)

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        for fac in [2,3,5]:
            while n%fac==0:
                n//=fac
        return n==1
sol=Solution()
x=int(input("Enter number: "))
print(sol.isUgly(x)) 
                  
