# Problem NO: 10

# LeetCode: 344

# Problem: Reverse String

# Pattern: Strings + Two Pointers

# Brute Force:
# Create a new reversed string or use built-in reverse methods.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimal Approach:
# Use two pointers, one at the beginning and one at the end of the list. Swap the characters and move both pointers toward the center until they meet.
# Time Complexity: O(n)
# Space Complexity: O(1)

# What I Learned:
# Two pointers can efficiently reverse a string in place by swapping characters from both ends. This avoids creating an additional string or list and uses constant extra space.

# CODE:    
class Solution(object):
    def reverseString(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1     
