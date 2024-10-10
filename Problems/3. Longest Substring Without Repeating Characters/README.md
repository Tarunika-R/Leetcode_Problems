# 3. Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

### Examples:

#### Example 1:
- **Input**: `s = "abcabcbb"`
- **Output**: `3`
- **Explanation**: The answer is `"abc"`, with the length of 3.

#### Example 2:
- **Input**: `s = "bbbbb"`
- **Output**: `1`
- **Explanation**: The answer is `"b"`, with the length of 1.

#### Example 3:
- **Input**: `s = "pwwkew"`
- **Output**: `3`
- **Explanation**: The answer is `"wke"`, with the length of 3.
  - Notice that the answer must be a substring, `"pwke"` is a subsequence and not a substring.

---

## Approach

The problem can be solved efficiently using the **Sliding Window** technique, which helps us maintain a window of the longest substring without repeating characters as we traverse through the string.

### Steps:
1. Use two pointers, `left` and `right`, to represent the current window of the substring.
2. A **set** is used to keep track of the unique characters within the current window.
3. Start by moving the `right` pointer across the string:
   - If the character at `right` is already in the set, slide the `left` pointer to remove characters from the window until the duplicate character is removed.
   - If it's not a duplicate, add it to the set and check if the current window is the longest by comparing it to the maximum length found so far.
4. Repeat until the `right` pointer reaches the end of the string.
5. Return the maximum length of the substring found.

### Time Complexity:
- The time complexity is **O(n)**, where `n` is the length of the string `s`. Each character is processed at most twice (once by `right` pointer and once by `left` pointer).

### Space Complexity:
- The space complexity is **O(k)**, where `k` is the size of the character set used in the input string (which depends on the number of distinct characters).


