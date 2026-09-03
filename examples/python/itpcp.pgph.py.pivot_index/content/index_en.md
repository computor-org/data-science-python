# Finding the Pivot Index

## Introduction

### Pivot Index

The pivot index is the index where the sum of all numbers strictly to the left of the index is equal to the sum of all numbers strictly to the right of the index.

If the index is at the left edge of the array, the left sum is 0 because there are no elements to its left. This also applies to the right edge of the array.

## Task

1. Given an array of integers `nums`. Write a function that returns the leftmost pivot index of the array.

2. Return the leftmost pivot index. If no such index exists, -1 should be returned.

## Hints


**Example 1:**

    Input: `nums = [1,7,3,6,5,6]`

    Output: `3`

    Explanation:

    The pivot index is 3.

    Left sum = `nums[0] + nums[1] + nums[2]` = 1 + 7 + 3 = 11

    Right sum = `nums[4] + nums[5]` = 5 + 6 = 11

**Example 2:**

    Input: `nums = [1,2,3]`

    Output: `-1`

    Explanation:

    There is no index that satisfies the conditions in the problem statement.

**Example 3:**

    Input: `nums = [2,1,-1]`

    Output: `0`

    Explanation:

    The pivot index is 0.

    Left sum = 0 (no elements to the left of index 0)

    Right sum = `nums[1] + nums[2]` = 1 + -1 = 0
