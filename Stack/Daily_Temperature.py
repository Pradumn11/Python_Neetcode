# Daily Temperatures
#
# Given an array of integers temperatures represents the daily temperatures, return an array answer
# such that answer[i] is the number of days you have to wait after the ith day to get a warmer
# temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution(object):
    def dailyTemperatures(self, temperatures):

        stack = []
        arr = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while (stack and t > stack[-1][0]):
                stackNum, stackIndex = stack.pop()
                arr[stackIndex] = i - stackIndex

            stack.append([t, i])

        return arr


a = Solution()
print(a.dailyTemperatures([1, 2, 1, 1, 4]))
