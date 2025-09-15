class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2 
            half = (mid - left) % 2 == 0

            if nums[mid] == nums[mid + 1]:
                if half:
                    left = mid + 2
                else:
                    right = mid - 1

            elif nums[mid] == nums[mid - 1]:
                if half:
                    right = mid - 2
                else:
                    left = mid + 1
            
            else:
                return nums[mid]

        return nums[left]
