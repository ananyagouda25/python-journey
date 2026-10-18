## Program: Prints the Pascal's triangle in the form of a list. Number of rows is taken from user.
# Given an integer numRows, return the first numRows of Pascal's triangle.
## In Pascal's triangle, each number is the sum of the two numbers directly above it 
## Time complexity: O(n^2)
## Space complexity: O(n^2)

# Method 2:
# Can do it in a diff way too. Use prev row's indexes to generate new/current row.
# Both have same time and space complexities.

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        i=0
        curr=1
        b=[]
        while i<numRows:
            j=0
            a=[]
            while j<=i:
                if j==0:
                    curr=1
                else:
                    curr=curr*(i-j+1)//j
                j+=1
                a.append(curr)
            b.append(a)
            i+=1
        return b
sol=Solution()
print(sol.generate(5))
