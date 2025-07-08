class Solution(object):
    def intToRoman(self, val):
        """
        :type num: int
        :rtype: str
        """
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD",
            "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL",
            "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV",
            "V", "VI", "VII", "VIII", "IX"]

        # Converting to roman
        thousands = m[val // 1000]
        hundreds = c[(val % 1000) // 100]
        tens = x[(val % 100) // 10]
        ones = i[val % 10]

        ans = thousands + hundreds + tens + ones

        return ans