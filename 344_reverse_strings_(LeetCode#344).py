## Program: Write a function that reverses a string. The input string is given as an array of characters s.
## You must do this by modifying the input array in-place with O(1) extra memory.
## Time complexity: O(n^2)
## Space complexity: O(1)

class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s)):
            a=s.pop()
            s.insert(i,a)
