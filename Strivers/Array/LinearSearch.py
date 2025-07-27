class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
        
def main():
    nums = [1, 2, 3, 4, 5]
    target = 3
    solution = Solution()
    result = solution.linearSearch(nums, target)
    print(result)

if __name__ == "__main__":
    main()