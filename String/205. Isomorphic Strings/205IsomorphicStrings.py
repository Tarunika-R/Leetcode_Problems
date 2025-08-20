class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        values = set()

        for i, char in enumerate(s):
            if char not in d:
                if t[i] in values:
                    return False
                d[char] = t[i]
                values.add(t[i])

            else:
                if t[i] != d[char]:
                    return False
        return True
