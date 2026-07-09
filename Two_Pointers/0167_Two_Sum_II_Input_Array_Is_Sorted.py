# Problem NO: 25
# LeetCode: 167
# Problem: Two Sum II - Input Array Is Sorted
# Pattern: Two Pointers

# Brute Force:
# Use two loops to check every possible pair.
# For each number, check all remaining numbers and find the pair whose sum equals target.

# Time Complexity: O(n²)
# Space Complexity: O(1)


# Optimal Approach 1:
# Use a HashMap to store visited numbers and their indexes.
# For every number, calculate target - current number.
# If the required number already exists in the HashMap, return both indexes.

# Time Complexity: O(n)
# Space Complexity: O(n)


# More Optimized Approach:
# Use Two Pointers because the input array is already sorted.

# Place one pointer at the beginning and one pointer at the end.
# Calculate the sum of both pointer values.

# If sum is greater than target:
# Move the right pointer left to get a smaller value.

# If sum is less than target:
# Move the left pointer right to get a bigger value.

# If sum equals target:
# Return both indexes.

# Time Complexity: O(n)
# Space Complexity: O(1)


# What I Learned:
# I learned that sorted array problems can often be solved using the Two Pointer technique.
# HashMap can reduce time complexity, but it uses extra space.
# Using the sorted property helps achieve O(n) time with O(1) space.


# CODE:

class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1

        while l < r:
            total = numbers[l] + numbers[r]

            if total > target:
                r -= 1

            elif total < target:
                l += 1

            else:
                return [l+1, r+1]
