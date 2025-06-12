class Solution:
    def minAddToMakeValid(self, s):
        # Initialize counters for the open and close parentheses needed
        open_needed = 0  # Tracks unmatched '('
        close_needed = 0  # Tracks unmatched ')'
        
        # Iterate through the string
        for char in s:
            if char == '(':
                open_needed += 1  # We need a matching ')' for this '('
            else:  # char == ')'
                if open_needed > 0:
                    open_needed -= 1  # Match it with a previous '('
                else:
                    close_needed += 1  # We need an extra '(' for this ')'
        
        # The result is the total unmatched parentheses
        return open_needed + close_needed

        