## Program: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
## In Pascal's triangle, each number is the sum of the two numbers directly above it.
## Time complexity: O(n^2)
## Space complexity: O(n^2)

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        i=0
        curr=1
        b=[]
        while i<=rowIndex:
            j=0
            a=[]
            while j<=i:
                if j==0:
                    curr=1
                else:
                    curr=curr*(i-j+1)//j
                a.append(curr)
                j+=1
            i+=1
            b.append(a)
        return b[rowIndex]
sol=Solution()
print(sol.getRow(3))


## Other version:
## Time complexity: O(n^2)
## Space complexity: O(n)

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        i=0
        curr=1
        while i<=rowIndex:
            j=0
            a=[]
            while j<=i:
                if j==0:
                    curr=1
                else:
                    curr=curr*(i-j+1)//j
                a.append(curr)
                j+=1
            i+=1
        return a
