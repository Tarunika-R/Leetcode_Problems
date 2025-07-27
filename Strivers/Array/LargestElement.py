class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        for num in nums:
            if num > largest:
                largest = num
        return largest
                
def main():
    nums = [3, 1, 4, 1, 5, 9, 2]
    solution = Solution()
    print(solution.largestElement(nums))  # Output: 5

if __name__ == "__main__":
    main()