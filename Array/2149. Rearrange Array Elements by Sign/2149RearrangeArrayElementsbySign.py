class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result