class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = {}
        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        # for num in count:
        #     if count[num] > len(nums) // 2:
        #         return num
                
        count = Counter(nums)
        n = len(nums)

        for key, values in count.items():
            if values > n // 2:
                return key