class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        
        for i in range(n):
            mid = (low + high) // 2
            left = nums[mid - 1] if mid - 1 >= 0 else float('-inf') 
            right = nums[mid + 1] if mid + 1 < n else float('-inf')

            if nums[mid] > left and nums[mid] > right:
                return mid
            elif nums[mid] < right: 
                low = mid + 1 
            else:
                high = mid - 1
        return -1

            
