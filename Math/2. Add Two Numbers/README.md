# 2. Add Two Numbers

## Description

The "Add Two Numbers" problem requires you to add two non-negative integers represented by linked lists. The digits are stored in reverse order, meaning that the least significant digit comes first. Each node in the linked list contains a single digit.

## Problem Statement

Given two non-empty linked lists representing two non-negative integers, add the two numbers and return the sum as a linked list.

### Example Inputs and Outputs

- **Example 1**
  - **Input:** `l1 = [2, 4, 3], l2 = [5, 6, 4]`
  - **Output:** `[7, 0, 8]`
  - **Explanation:** `342 + 465 = 807`, represented as the linked list `[7, 0, 8]`.

- **Example 2**
  - **Input:** `l1 = [0], l2 = [0]`
  - **Output:** `[0]`

- **Example 3**
  - **Input:** `l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]`
  - **Output:** `[8, 9, 9, 9, 0, 0, 0, 1]`
  - **Explanation:** `9999999 + 9999 = 10009998`, represented as the linked list `[8, 9, 9, 9, 0, 0, 0, 1]`.

### Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Algorithm

To solve the problem, we can iterate through both linked lists simultaneously, summing the corresponding digits while also managing any carry from previous additions.

### Steps

1. Initialize a new linked list to store the result and a pointer for the current node in the result list.
2. Initialize a variable to store the carry (initially set to 0).
3. While there are still nodes to process in either linked list:
   - Extract the values from the current nodes of `l1` and `l2` (defaulting to 0 if a list is exhausted).
   - Calculate the sum of these values and the carry.
   - Update the carry for the next iteration.
   - Create a new node in the result linked list with the digit value of the sum modulo 10.
   - Move the current pointers in the input and result lists forward.
4. If there is any carry left after processing both lists, add a new node with the carry value.
5. Return the head of the resulting linked list.

## Installation

To run the solution, ensure you have Python installed on your machine. You can use any standard Python environment or IDE.

## Usage

1. Clone the repository:
   ```bash
   git clone <repository-url>
