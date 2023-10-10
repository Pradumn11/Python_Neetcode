# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]




# class Solution(object):
#     def generateParenthesis(self, n):
#
#         list = []
#
#         def backtrack(str, openC, closedC, n):
#
#             if n * 2 == len(str):
#                 list.append(str)
#
#             if openC < n:
#                 backtrack((str + "("), openC + 1, closedC, n)
#
#             if closedC < openC:
#                 backtrack((str + ")"), openC, closedC + 1, n)
#
#         backtrack("", 0, 0, n)
#         return list
#
