class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        length = 0

        for i in range(n):
            for j in range(i, n):
                s = 0

                for K in range(i, j + 1):
                    s += nums[K]

                if s == k:
                    length = max(length, j - i + 1)
        return length
        
    
def main():
    nums = [2, -3, 1, 1]
    k = 2
    solution = Solution()
    print(solution.longestSubarray(nums, k))

if __name__ == "__main__":
    main()