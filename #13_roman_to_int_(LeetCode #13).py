# Program: It converts the roman number notation into numerical/integer value.

class Solution:
    def romanToInt(self, s: str) -> int:
        tot=0
        num={'L': 50,'I': 1,'X': 10,'C': 100,'V': 5,'D': 500,'M': 1000}
        for i in range(1,len(s)):
            curr=num[s[i]]
            prev=num[s[i-1]]
            if prev>=curr:
                tot+=prev
            else:
                tot-=prev
        tot+=num[s[-1]]
        return tot
work=Solution()
heh=input("Enter a roman number: ")
print(work.romanToInt(heh))
