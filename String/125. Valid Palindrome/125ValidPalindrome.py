class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]