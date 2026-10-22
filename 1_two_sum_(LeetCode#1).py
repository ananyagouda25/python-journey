## Program: You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## Time complexity: O(n^2)
## Space complexity: O(1)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


## Optimised Solution:
## Time complexity: O(n)
## Space complexity: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i in range(0,len(nums)):
            x=target-nums[i]
            if x in seen:
                return [seen[x],i]
            seen[nums[i]]=i
        
