# Program: Checks if entered input is a palindrome or not. 
# Concepts: strings, isalnum(), lower(), slicing
# Time: O(n) | Space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        heh=''
        for i in s:
            if i.isalnum():
                heh+=i.lower()
        return heh==heh[::-1]
cal=Solution()
que=input("Enter input: "))
print(cal.isPalindrome(que))
