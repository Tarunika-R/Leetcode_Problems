from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)   # Count frequency of each character
        sorted_char = sorted(s, key = lambda ch:(-freq[ch], ch))
        return "".join(sorted_char)