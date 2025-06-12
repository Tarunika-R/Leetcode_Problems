# Longest Palindromic Substring

## Problem Description

Given a string `s`, return the longest **palindromic substring** in `s`.

### Examples

#### Example 1:
- **Input:** `s = "babad"`
- **Output:** `"bab"`
- **Explanation:** `"aba"` is also a valid answer.

#### Example 2:
- **Input:** `s = "cbbd"`
- **Output:** `"bb"`

### Constraints
- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters.

---

## Approach

### Steps:
1. **Expand Around Center**: 
   - The idea is to expand around each character (or between two consecutive characters) to find the longest palindromic substring. 
   - We do this for both odd-length and even-length palindromes by checking all possible centers.
   
2. **Helper Function**:
   - A helper function `expandAroundCenter` is used to expand around the center and check for the longest palindrome at that center. This function will return the longest palindrome by expanding outwards from the center until the characters on both sides are no longer equal.

3. **Main Loop**:
   - We iterate through each character in the string and treat it as a potential center for a palindrome.
   - For each character, we check for two types of centers: 
     - One with the center at a single character (odd-length palindromes).
     - Another with the center between two characters (even-length palindromes).
   
4. **Comparison and Update**:
   - After checking all possible centers, we keep track of the longest palindromic substring found and return it as the result.

### Time Complexity
- **Time Complexity:** O(n²), where `n` is the length of the input string. The reason for this is that for each character, we are expanding outwards to find the longest palindrome, which takes O(n) time in the worst case.

---