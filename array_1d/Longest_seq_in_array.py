# Longest Consecutive Sequence
#
# Given an unsorted array of integers nums, return the length of the longest consecutive
# elements sequence.
#
# You must write an algorithm that runs in O(n) time.


class Solution(object):
    def longestConsecutive(self, nums):

        numset = set(nums)
        total = 0

        for n in nums:

            if (n - 1) not in numset:
                length = 0
                while (n + length) in numset:
                    length += 1
                total = max(length, total)

        return total