class Solution:
    def maxWidthRamp(self, nums):
        # Create a list to store indices of the decreasing sequence
        stack = []
        
        # Traverse the array to populate the stack with decreasing elements' indices
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        max_width = 0
        
        # Traverse the array in reverse to calculate the maximum width ramp
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())
        
        return max_width
