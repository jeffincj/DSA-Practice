# LeetCode: 509

# Problem: Fibonacci Number

# Pattern: Recursion

# Brute Force: Recursively calculate Fibonacci numbers by calling fib(n-1) and fib(n-2) until reaching the base cases.

# Time Complexity: O(2^n)

# Optimal Approach: This solution uses simple recursion with base cases. Although accepted, it recalculates the same subproblems multiple times. A better approach is Dynamic Programming (Memoization/Tabulation) for O(n) time.

# Time Complexity: O(2^n)

# Space Complexity: O(n)   # Due to recursion call stack

# What I Learned: I learned how recursion works by breaking a problem into smaller subproblems and using base cases to stop recursive calls. I also understood that simple recursion is inefficient because it repeats many calculations, and Dynamic Programming can optimize it.

# CODE:
class Solution(object):
    def fib(self, n):
        if n == 1:
            return 1
        elif n == 0:
            return 0
        return self.fib(n - 1) + self.fib(n - 2)
