## Program: Given an integer x, return true if x is a palindrome, and false otherwise.
## Time complexity: O(n)
## Space complexity: O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x==x[::-1]:
            return True
        else:
            return False
