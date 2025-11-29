# Two Sum (Array / Hashmap)

## Problem
Given an array `nums` and a target value, return the indices of the two numbers that add up to the target.

## Example
Input:
nums = [2, 7, 11, 15]  
target = 9

Output:
[0, 1]

## Approach (Hashmap – O(n))
- Loop through the list.
- For each number, check if its complement (`target - num`) is already seen.
- Store the number with its index in a dictionary.
- Return the pair when found.

## Complexity
- Time: O(n)
- Space: O(n)
