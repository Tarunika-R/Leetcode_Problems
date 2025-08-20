class Solution(object):
    def twoSum(self, nums, target):
        # num_dict = {}  
        # for i, num in enumerate(nums):
        #     diff = target - num 
        #     if diff in num_dict:
        #         return [num_dict[diff], i] 
        #     num_dict[num] = i

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []