# Problem: Matrix diagonal sum (both primary and secondary)
# Time complexity: O(N)
# Space complexity: O(1)

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sumy=0
        for i in range(0,len(mat)):
            sumy+=mat[i][i]
            sumy+=mat[len(mat)-i-1][i]
        if (len(mat)%2==1):
            sumy-=mat[len(mat)//2][len(mat)//2]
        return sumy
sol=Solution()
print(sol.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
