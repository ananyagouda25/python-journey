# Program: LeetCode #242 - Valid Anagram
# Approach 1: Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n) (Python's sorted creates a new list)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

# Orrrr... below is the chatgpt version..
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True
