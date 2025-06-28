class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Initialize the pointer for non-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move the non-val element to the correct position
                k += 1  # Increment the non-val pointer
        return k 