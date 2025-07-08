class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize base cases
        first, second = 1, 2
        
        # Compute ways for steps 3 to n
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
        
        return second
