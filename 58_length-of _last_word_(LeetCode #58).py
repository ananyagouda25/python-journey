# Program: Checks and returns the length of the last word.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=-1
        count=0
        while i>=-len(s) and s[i]==' ':
            i-=1
        while i>=-len(s) and s[i]!=' ':
            count+=1
            i-=1
        return count
sol=Solution()
print(sol.lengthOfLastWord('   fly me   to   the moon  '))
