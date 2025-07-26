class Solution:
    def secondLargestElement(self, nums):
        largest = second_largest = float('-inf')
        for n in nums:
            if n > largest:
                second_largest = largest
                largest = n
            elif n > second_largest and n != largest:
                second_largest = n
        print(second_largest)

def main():
    nums = [3, 1, 4, 1, 5, 9, 2, 8]
    solution = Solution()
    solution.secondLargestElement(nums)

if __name__ == "__main__":
    main()
                