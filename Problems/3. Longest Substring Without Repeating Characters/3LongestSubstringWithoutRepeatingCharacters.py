class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Create a set to store the unique characters in the current window
        char_set = set()
        
        # Initialize two pointers and the maximum length variable
        left = 0
        max_len = 0
        
        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If the character is already in the set, remove the left character
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set and update the maximum length
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len