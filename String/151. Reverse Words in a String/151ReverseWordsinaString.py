class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        word = s.split()
        reversed_words = word[::-1]
        return " ".join(reversed_words)