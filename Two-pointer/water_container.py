# Container With Most Water
#
# You are given an integer array height of length n. There are n vertical lines drawn such
# that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container
# contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.


class Solution(object):
    def maxArea(self, height):

        i, j = 0, len(height) - 1
        max1 = 0

        while i < j:
            min_size = min(height[i], height[j])
            max1 = max(max1, (j - i) * min_size)

            if (height[i] < height[j]):
                i += 1
            elif (height[j] < height[i]):
                j -= 1
            else:
                i += 1
                j -= 1

        return max1

    """
    :type height: List[int]
    :rtype: int
    """
