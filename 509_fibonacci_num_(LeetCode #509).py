# Problem: LeetCode 509 - Fibonacci Number
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        prev,curr=0,1
        for i in range(1,n):
            tot=prev+curr
            prev=curr
            curr=tot
        return curr
call=Solution()
n=int(input("n = "))
print(call.fib(n))
        


        
