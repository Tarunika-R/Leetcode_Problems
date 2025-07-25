class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
            
        mid = len(nums)//2
        L = nums[:mid]
        R = nums[mid:]

        self.mergeSort(L)
        self.mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
        
        return nums
    
def main():
    nums =  [7, 4, 1, 5, 3]
    solution = Solution()
    sorted_nums = solution.mergeSort(nums)
    print("Sorted array:", sorted_nums)

if __name__ == "__main__":
    main()