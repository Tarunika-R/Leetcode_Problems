class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        position = 0

        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1

        while position < len(nums):
            nums[position] = 0
            position += 1

# def main():
#     nums = [0, 1, 0, 3, 12]
#     solution = Solution()
#     solution.moveZeroes(nums)
#     print(nums)  # Output: [1, 3, 12, 0, 0]

# if __name__ == "__main__":
#     main()