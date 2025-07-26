class Solution:
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key        
        return nums                

def main():
    nums =  [7, 4, 1, 5, 3]
    solution = Solution()
    sorted_nums = solution.insertionSort(nums)
    print("Sorted array:", sorted_nums)

if __name__ == "__main__":
    main()