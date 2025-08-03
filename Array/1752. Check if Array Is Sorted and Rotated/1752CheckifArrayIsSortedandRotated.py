class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count >  1:
                    return False
        return True
# def main():
#     nums = [3, 4, 5, 1, 2]
#     solution = Solution()
#     print(solution.check(nums))  # Output: True

# if __name__ == "__main__":
#     main()