# Problem: Contains Duplicate II

# LeetCode: 219

# Pattern: Array + HashMap + Index Tracking

# Brute Force:
# Compare every element with all following elements and check:
# 1. If the values are equal
# 2. If their index difference is <= k

# Time Complexity: O(n²)

# Optimal Approach:
# Use a HashMap to store the last seen index of each number.
# If the current number already exists in the HashMap,
# calculate the distance between indices.
# If the distance is <= k, return True.

# Time Complexity: O(n)

# Space Complexity: O(n)

# What I Learned:
# A HashMap can store both a value and its index.
# By storing the last seen index of each element,
# we can instantly calculate the distance between duplicates
# without checking all previous elements.
# This reduces the complexity from O(n²) to O(n).

# CODE:

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                if (i - seen[num]) <= k:
                    return True

            seen[num] = i

        return False
