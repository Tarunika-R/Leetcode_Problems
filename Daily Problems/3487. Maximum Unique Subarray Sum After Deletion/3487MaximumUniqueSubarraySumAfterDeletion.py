# class Solution(object):
#     def maxSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         seen = set()
#         left = 0
#         curr_sum = 0
#         max_sum = 0

#         for right in range(len(nums)):
#             while nums[right] in seen:
#                 seen.remove(nums[left])
#                 curr_sum -= nums[left]
#                 left += 1

#             seen.add(nums[right])
#             curr_sum += nums[right]
#             max_sum = max(max_sum, curr_sum)

#         return max_sum

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveNumsSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet)