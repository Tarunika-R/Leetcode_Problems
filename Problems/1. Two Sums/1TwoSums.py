class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}  
        for i, num in enumerate(nums): # enumerate: to iterate through a sequence and keep track of the index of each element
            diff = target - num 
            if diff in num_dict:
                return [num_dict[diff], i] 
            num_dict[num] = i
        