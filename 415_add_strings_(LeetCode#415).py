## Program: Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
## You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
## You must also not convert the inputs to integers directly.
## Time complexity: O(max(len(num1),len(num2))
## Space complexity: O(max(len(num1),len(num2))


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a=[]
        k=0
        i=len(num1)-1
        j=len(num2)-1
        while(i>=0 or j>=0 or k>0):
            if i>=0:
                d1=int(num1[i])
            else:
                d1=0
            if j>=0:
                d2=int(num2[j])
            else:
                d2=0
            tot=d1+d2+k
            k=tot//10
            l=tot%10
            a.append(str(l))
            j-=1
            i-=1
        return "".join(a[::-1])

