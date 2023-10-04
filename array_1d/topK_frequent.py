class Solution(object):
    def topKFrequent(self, nums, k):

        frequency = {}
        for num in nums:

            if num not in frequency:

                frequency[num] = 1

            else:

                frequency[num] = frequency[num] + 1
        frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

        result = list(frequency.keys())[:k]

        return result



    def topKFrequent_v2(self, nums, k):

            count = {}

            freq = [[] for i in range(len(nums) + 1)]

            for n in nums:
                count[n] = count.get(n, 0) + 1

            for n, c in count.items():
                freq[c].append(n)

            res = []
            for j in range(len(freq) - 1, 0, -1):
                for n in freq[j]:
                    res.append(n)
                    if len(res) == k:
                        return res

            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """

    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
