# Median of Two Sorted Arrays

## Problem Description

You are given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively. The task is to return the **median** of the two sorted arrays. The overall runtime complexity should be `O(log(m + n))`.

### Examples

#### Example 1:
- **Input:** `nums1 = [1, 3]`, `nums2 = [2]`
- **Output:** `2.00000`
- **Explanation:** The merged array is `[1, 2, 3]` and the median is `2`.

#### Example 2:
- **Input:** `nums1 = [1, 2]`, `nums2 = [3, 4]`
- **Output:** `2.50000`
- **Explanation:** The merged array is `[1, 2, 3, 4]` and the median is `(2 + 3) / 2 = 2.5`.

### Constraints
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

---

## Approach

### Steps:
1. **Optimal Logarithmic Search**: 
    - The approach uses binary search on the smaller array to partition both arrays such that the left partition contains elements smaller than or equal to the right partition. This ensures we can directly compute the median.
    - The key idea is to ensure the partitions are balanced in size and values, and from there, the median is easily computed based on the partitioning.

2. **Median Calculation**:
    - If the combined length of the arrays is odd, the median is the maximum value from the left partition.
    - If the combined length is even, the median is the average of the maximum value from the left partition and the minimum value from the right partition.

### Time Complexity
- **Time Complexity:** `O(log(min(m, n)))` where `m` and `n` are the sizes of the two input arrays. This satisfies the required `O(log(m + n))` complexity.

---