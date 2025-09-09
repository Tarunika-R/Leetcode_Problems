class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        ans = []

        while low <= high:
            mid = (low + high) // 2

            if nums[low] <= nums[high]: # usual sorted array
                ans = min(ans, nums[low])
                break

            if nums[low] <= nums[mid]: # if left part is sorted
                ans = min(ans, nums[low])
                low = mid + 1 # remove left side of array
            else: # if right part is sorted
                ans = min(ans, nums[mid]) 
                high = mid - 1
        return ans 