class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        result = []
        n = len(nums)
        for i in count:
            if count[i] > n/3:
                result.append(i)
        return result
        
        
    