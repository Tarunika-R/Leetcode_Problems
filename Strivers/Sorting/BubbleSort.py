class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        swap = False
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    
                    swap = True
            if not swap:
                break
        return nums
    
def main():
    nums =  [7, 4, 1, 5, 3]
    solution = Solution()
    sorted_nums = solution.bubbleSort(nums)
    print("Sorted array:", sorted_nums)

if __name__ == "__main__":
    main()


# Worst case time complexity: O(n^2)
# Best case time complexity: O(n)
# best case includes adding break to non sorted array