class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        m = len(queries)
        
        # Step 1: Count how many times each index is covered
        coverage = [0] * (n + 1)
        for l, r in queries:
            coverage[l] += 1
            if r + 1 < n:
                coverage[r + 1] -= 1

        for i in range(1, n):
            coverage[i] += coverage[i - 1]

        # Step 2: Check if it's possible at all
        for i in range(n):
            if coverage[i] < nums[i]:
                return -1  # Impossible to make nums[i] zero

        # Step 3: Count how many queries we can remove greedily (from the end)
        needed = nums[:]  # How much we still need to decrement
        result = 0
        used = [0] * n  # Tracks how many decrements we still need per index

        # Apply all queries
        for l, r in queries:
            for i in range(l, r + 1):
                used[i] += 1

        # Try to remove queries from the end
        for i in range(m - 1, -1, -1):
            l, r = queries[i]
            removable = True
            for j in range(l, r + 1):
                if used[j] <= needed[j]:
                    removable = False
                    break
            if removable:
                result += 1
                for j in range(l, r + 1):
                    used[j] -= 1

        return result