class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            sums = numbers[left] + numbers[right]
            print(sums)
            if sums == target:
                return [left + 1, right + 1]
            elif sums > target:
                right -= 1
            elif sums < target:
                left += 1
        return []
            