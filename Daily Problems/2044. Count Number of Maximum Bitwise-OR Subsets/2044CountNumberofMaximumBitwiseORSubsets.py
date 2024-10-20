class Solution(object):
    def countMaxOrSubsets(self, nums):
        max_or = 0
        for num in nums:
            max_or |= num

        def count_subsets(i, current_or):
            if i == len(nums):
                return 1 if current_or == max_or else 0
            return count_subsets(i + 1, current_or | nums[i]) + count_subsets(i + 1, current_or)

        return count_subsets(0, 0)
        