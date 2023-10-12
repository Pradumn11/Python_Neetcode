# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def search(self, nums, target):

        i, j = 0, len(nums)

        while (i < j):
            mid = (i + j) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid
            else:
                i = mid + 1

        return -1
