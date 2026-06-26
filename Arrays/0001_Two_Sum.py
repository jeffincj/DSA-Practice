# Problem NO: 3

# LeetCode: 1

# Problem: Two Sum

# Pattern: Array + HashMap (Complement Lookup)

# Brute Force: Check every pair of elements using nested loops to find the target sum.

# Time Complexity: O(n²)

# Optimal Approach: Use a HashMap to store previously seen numbers and their indices. For each element, calculate the required complement (target - current number). If the complement exists in the HashMap, return the indices.

# Time Complexity: O(n)

# Space Complexity: O(n)

# What I Learned: Instead of checking every pair, I can calculate the required complement and use a HashMap for O(1) lookups. This reduces the overall complexity from O(n²) to O(n).

# CODE:
class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i,num in enumerate(nums):
            n=target-num
            if n in seen:
                return seen[n],i
            seen[num]=i
