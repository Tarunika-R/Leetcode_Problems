class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # Step 1: Remove leading whitespace
        
        if not s:
            return 0  # If string is empty after removing spaces

        sign = 1  # Assume positive by default
        i = 0     # Index to traverse the string

        # Step 2: Check for sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        num = 0

        # Step 3: Read digits and form the number
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = sign * num  # Step 4: Apply the sign

        # Step 5: Clamp the result to the 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
