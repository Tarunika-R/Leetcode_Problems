# Minimum Moves to Make Parentheses Valid

## Problem Statement

A parentheses string is valid if and only if:
1. It is the empty string.
2. It can be written as `AB` (A concatenated with B), where A and B are valid strings.
3. It can be written as `(A)`, where A is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

For example, if `s = "()))"`, you can insert an opening parenthesis to become `"(()))"` or a closing parenthesis to become `"())))"`.

### Objective

Return the **minimum number of moves** required to make `s` valid.

---

## Examples

### Example 1:
```bash
Input: s = "())"
Output: 1
```

## Approach
We use a counting approach to track the number of unmatched parentheses. Specifically, we track:

Unmatched opening parentheses: The number of '(' that need to be closed.
Unmatched closing parentheses: The number of ')' that need to be opened (i.e., when we encounter ')' but don't have a matching '(').

### Steps:
1. Initialize two counters:
    - open_needed for tracking unmatched opening parentheses.
    - close_needed for tracking unmatched closing parentheses.
2. Traverse the string:
    - For every '(', increment open_needed because it needs a matching closing parenthesis.
    - For every ')', check if there is an unmatched '(' to pair it with:
        - If yes, decrement open_needed to match the parentheses.
        - If no, increment close_needed because an extra opening parenthesis will be required to make it valid.
3. The total moves required to make the string valid will be the sum of open_needed and close_needed.

--- 

## Time Complexity:
O(n), where n is the length of the string. We iterate through the string once.

---

## Space Complexity:
O(1), as we only use constant space for the counters.