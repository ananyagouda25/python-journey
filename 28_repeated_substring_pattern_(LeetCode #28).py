# Program: Repeated Substring Pattern in two substrings
# Time: O(n x m)  where m and n are lengths of two substrings
# Space: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

sl=Solution()
print(sl.strStr('leetcode','leeto'))
