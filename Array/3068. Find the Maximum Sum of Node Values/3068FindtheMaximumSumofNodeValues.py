class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        base_sum = sum(nums)
        gains = []

        # Compute gain for each node if we flip it
        for val in nums:
            gain = (val ^ k) - val
            gains.append(gain)

        # Sort in descending order to pick top gains
        gains.sort(reverse=True)

        max_gain = 0
        i = 0

        # Choose best even number of flips with positive combined gain
        while i + 1 < len(gains) and gains[i] + gains[i + 1] > 0:
            max_gain += gains[i] + gains[i + 1]
            i += 2

        return base_sum + max_gain
