class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # Check if first row needs to be zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check if first column needs to be zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Update cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0