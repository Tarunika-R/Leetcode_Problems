# Maximum Swap

## Problem Description

You are given an integer `num`. You can swap two digits **at most once** to get the maximum valued number.

Your task is to return the maximum number that can be obtained by performing this operation.

### Examples

#### Example 1:
- **Input:** `num = 2736`
- **Output:** `7236`
- **Explanation:** By swapping the digits `2` and `7`, the number becomes `7236`, which is the maximum possible number after one swap.

#### Example 2:
- **Input:** `num = 9973`
- **Output:** `9973`
- **Explanation:** No swap can increase the value of the number, so the original number is returned.

### Constraints
- `0 <= num <= 10^8`

---

## Approach

### Steps:
1. **Convert to List:** The number is converted into a list of its digits, making it easier to perform swaps.
2. **Track Last Occurrences:** We store the last occurrence index of each digit (0-9) in the number, which helps in deciding where to swap for maximizing the value.
3. **Find Best Swap:** We traverse through each digit of the number and, for each digit, check if a larger digit exists in the later part of the list. If a larger digit is found, we swap them and return the new number.
4. **Return Result:** If no larger digit is found to make a beneficial swap, the original number is returned.

---

