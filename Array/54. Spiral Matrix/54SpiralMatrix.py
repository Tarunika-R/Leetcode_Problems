class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        n = len(matrix) # no. of rows
        m = len(matrix[0]) # no. of columns

        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        while top <= bottom and left <= right:
            # left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
