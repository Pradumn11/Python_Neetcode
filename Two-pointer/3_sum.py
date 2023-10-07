# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
# that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.


class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if (i > 0 and a == nums[i - 1]):
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if (threesum > 0):
                    r -= 1
                elif (threesum < 0):
                    l += 1
                else:
                    triplet = [a, nums[l], nums[r]]
                    res.append(triplet)
                    while l < r and nums[l] == triplet[1]:
                        l += 1

                    while nums[r] == triplet[2] and l < r:
                        r -= 1

        return res

        # """
        # :type nums: List[int]
        # :rtype: List[List[int]]
        # """
