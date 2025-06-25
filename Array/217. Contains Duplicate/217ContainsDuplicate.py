class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for item in nums:
            if item in seen:
                return True
            seen.add(item)
        return False 