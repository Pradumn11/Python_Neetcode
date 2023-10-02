# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters
# of a different word or phrase, typically using all the original letters exactly once.


# """
# :type s: str
# :type t: str
# :rtype: bool
# """
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    for j in count_s:
        if count_s[j] != count_t.get(j, 0):
            return False
    return True

