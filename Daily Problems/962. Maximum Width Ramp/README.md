# Maximum Width Ramp

## Problem Statement

A **ramp** in an integer array `nums` is a pair `(i, j)` where:
- `i < j`
- `nums[i] <= nums[j]`

The width of the ramp is defined as `j - i`.

Given an integer array `nums`, your task is to return the **maximum width** of a ramp in `nums`. If no ramp exists, return `0`.

---

## Examples

### Example 1:
- **Input**: nums = [6, 0, 8, 2, 1, 5]
- **Output**: 4
- **Explanation**: The maximum width ramp is achieved at (i, j) = (1, 5) with nums[1] = 0 and nums[5] = 5. The width is 5 - 1 = 4.
--- 

### Example 2:
- **Input**: nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
- **Output**: 7
- **Explanation**: The maximum width ramp is achieved at (i, j) = (2, 9) with nums[2] = 1 and nums[9] = 1. The width is 9 - 2 = 7.

---

# Constraints
- `2 <= nums.length <= 50,000`
- `0 <= nums[i] <= 50,000`

## Approach

### Problem Breakdown:
The goal is to find the largest distance (j - i) where:

i < j
nums[i] <= nums[j]

### Plan:
1. Store Decreasing Indices:
    We can first build a stack of indices where the array is decreasing. This will help us find potential starting points for ramps.
2. Reverse Traversal:
    After constructing the stack, we traverse the array from the end to the beginning. For each element, we check if it forms a valid ramp with any of the indices in the stack.
3. Compute Width:
    When a valid ramp is found, we compute the width j - i and keep track of the maximum width.

## Steps:
1. Initialize a stack: Store indices of elements forming a decreasing sequence.
2. Traverse the array from right to left to find valid ramps.
3. For each element, pop indices from the stack and compute the width if a valid ramp is found.