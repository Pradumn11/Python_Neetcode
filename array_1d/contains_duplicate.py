# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears
# at least twice in the array, and return false if every element is distinct.



# """
        # :type nums: List[int]
        # :rtype: bool
        # """

class Solution(object):
    def containsDuplicate(self, nums):

        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


