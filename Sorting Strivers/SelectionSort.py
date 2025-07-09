class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)):
            min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
        return nums

def main():
    nums =  [7, 4, 1, 5, 3]
    solution = Solution()
    sorted_nums = solution.selectionSort(nums)
    print("Sorted array:", sorted_nums)

if __name__ == "__main__":
    main()