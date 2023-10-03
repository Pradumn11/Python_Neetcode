class Solution(object):
    def twoSum(self, nums, target):

        hashmap = {}

        for i, n in enumerate(nums):
            a = target - n
            if nums[i] in hashmap:
                return [hashmap.get(nums[i]), i]

            hashmap[a] = i
        return []