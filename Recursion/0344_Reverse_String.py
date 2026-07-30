# LeetCode: 344

# Problem: Reverse String

# Pattern: Recursion + Two Pointers

# Brute Force: Create a new reversed string or use an extra array to store the characters in reverse order.

# Time Complexity: O(n)

# Optimal Approach: Use two pointers (left and right) with recursion. Swap the characters at both ends and recursively move the pointers toward the center until they meet.

# Time Complexity: O(n)

# Space Complexity: O(n)   # Due to recursion call stack

# What I Learned: I learned how recursion can be combined with the two-pointer technique to reverse a string in place. Each recursive call swaps one pair of characters and moves the pointers closer until the base case is reached.

# CODE:
class Solution(object):
    def reverseString(self, s):
        self.helper(s, 0, len(s) - 1)

    def helper(self, s, l, r):
        if l >= r:
            return s
        s[l], s[r] = s[r], s[l]
        return self.helper(s, l + 1, r - 1)
