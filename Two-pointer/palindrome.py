# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.


def isPalindrome(self, s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not self.alpha_num(s[left]):
            left += 1
        while right > left and not self.alpha_num(s[right]):
            right -= 1
        if (s[left].lower() != s[right].lower()):
            return False
        left += 1
        right -= 1

    return True


def alpha_num(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
