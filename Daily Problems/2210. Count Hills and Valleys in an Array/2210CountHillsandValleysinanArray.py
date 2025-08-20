class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        filtered = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                filtered.append(nums[i])
        
        count = 0
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1  # Hill
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1  # Valley
        
        return count

                 
