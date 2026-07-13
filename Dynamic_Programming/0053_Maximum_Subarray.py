# Problem NO: 29
# LeetCode: 53
# Problem: Maximum Subarray
# Pattern: Dynamic Programming (Kadane's Algorithm)

# Brute Force:
# Consider every possible subarray.
# Calculate the sum of each subarray.
# Return the maximum sum found.

# Time Complexity: O(n²)
# Space Complexity: O(1)


# Optimal Approach:
# Use Kadane's Algorithm.

# Keep two variables:
# 1. current_sum -> Maximum subarray sum ending at the current index.
# 2. max_sum -> Maximum subarray sum found so far.

# For every element:
# Compare:
# 1. Continue the current subarray (current_sum + current number)
# 2. Start a new subarray from the current number

# Choose the larger one as the new current_sum.
# Then update max_sum if current_sum becomes larger.

# Time Complexity: O(n)
# Space Complexity: O(1)


# What I Learned:
# I learned Kadane's Algorithm for solving Maximum Subarray.
# At every index, I only have two choices:
# Continue the existing subarray or start a new one.
# I do not need to store every subarray sum.
# Keeping only the current best sum and the overall best sum is enough.
# Initializing with nums[0] correctly handles arrays containing all negative numbers.


# CODE:

class Solution(object):
    def maxSubArray(self, nums):
        c_sum = nums[0]
        m_sum = nums[0]

        for i in range(1, len(nums)):
            if c_sum + nums[i] > nums[i]:
                c_sum += nums[i]
            else:
                c_sum = nums[i]

            m_sum = max(m_sum, c_sum)

        return m_sum
