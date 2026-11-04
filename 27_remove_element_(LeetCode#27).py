## Program: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
## Then return the number of elements in nums which are not equal to val.
## Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
## Time complexity: O(n)
## Space complexity: O(1)


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0
        for x in nums:
            if x!=val:
                nums[k]=x
                k+=1
        return k
