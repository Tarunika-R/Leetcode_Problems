# Two Sum Problem

## Description

The "Two Sum" problem requires you to find the indices of two numbers in an array of integers that add up to a given target. You may assume that each input will have exactly one solution, and you cannot use the same element twice. 

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

### Example Inputs and Outputs

- **Example 1**
  - **Input:** `nums = [2, 7, 11, 15], target = 9`
  - **Output:** `[0, 1]`
  - **Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

- **Example 2**
  - **Input:** `nums = [3, 2, 4], target = 6`
  - **Output:** `[1, 2]`

- **Example 3**
  - **Input:** `nums = [3, 3], target = 6`
  - **Output:** `[0, 1]`

### Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Follow-Up

Can you come up with an algorithm that has a time complexity of less than O(n²)?

## Algorithm

To solve the problem efficiently, we can use a hashmap (or dictionary) to store the difference between the target and each number as we iterate through the array. This approach allows us to find the two indices in a single pass, achieving O(n) time complexity.

### Steps

1. Initialize an empty hashmap to store the numbers and their corresponding indices.
2. Loop through the array:
   - For each number, calculate the difference between the target and the current number.
   - Check if the difference exists in the hashmap:
     - If it exists, return the current index and the index of the difference stored in the hashmap.
     - If it does not exist, store the current number and its index in the hashmap.
3. If no solution is found by the end of the loop, return an indication of failure (should not happen as per problem constraints).

## Installation

To run the solution, ensure you have Python installed on your machine. You can use any standard Python environment or IDE.

## Usage

1. Clone the repository:
   ```bash
   git clone <repository-url>
