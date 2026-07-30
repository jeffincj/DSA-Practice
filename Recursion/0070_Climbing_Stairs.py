# LeetCode: 70

# Problem: Climbing Stairs

# Pattern: Recursion

# Brute Force: Recursively calculate the number of ways to reach the top by taking either 1 or 2 steps at a time. At each step, explore both possibilities until the base cases are reached.

# Time Complexity: O(2^n)

# Optimal Approach: This solution uses simple recursion. However, it recalculates the same subproblems many times. A better approach is Dynamic Programming (Memoization or Tabulation), which reduces the time complexity to O(n).

# Time Complexity: O(2^n)

# Space Complexity: O(n)   # Due to recursion call stack

# What I Learned: I learned that a problem can be broken down into smaller subproblems using recursion. The number of ways to reach the nth stair depends on the ways to reach the (n-1)th and (n-2)th stairs. I also understood that recursion alone is inefficient because it repeatedly solves the same subproblems, making Dynamic Programming a much better solution.

# CODE:
class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
