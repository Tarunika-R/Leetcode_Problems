import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sum_ = 1
        sqrt = int(math.sqrt(num))
        for i in range(2, sqrt + 1):
            if num % i == 0:
                sum_ += i
                if i != num // i:
                    sum_ += num // i
        return num == sum_