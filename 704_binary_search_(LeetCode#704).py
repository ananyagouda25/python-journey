## Program: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
## If target exists, then return its index. Otherwise, return -1.
## Time complexity: O(log n) 
## Space complexity: O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                h=m-1
            else:
                l=m+1
        return -1
