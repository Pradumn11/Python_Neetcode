# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of
# a different word or phrase, typically using all the original letters exactly once.
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):

        hashmap = defaultdict(list)
        for s in strs:
            chars = [0] * 26

            for c in s:
                chars[ord(c) - ord('a')] += 1

            hashmap[tuple(chars)].append(s)
        return hashmap.values()
