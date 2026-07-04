# Problem NO: 14

# LeetCode: 541

# Problem: Reverse String II

# Pattern: String Traversal + Two Pointers + In-place Reversal

# Brute Force:

# Create a new string and manually reverse the first k characters for every 2k block.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimal Approach:

# Convert the string into a list because Python strings are immutable.

# Traverse the string in jumps of 2*k.

# For every block:

# Take the starting index
# Reverse only the first k characters
# Use two pointers:
# Left pointer at start
# Right pointer at min(start+k-1, len(s)-1)
# Swap characters until both pointers meet

# Time Complexity: O(n)
# Space Complexity: O(n)

# Python Optimization:

# Python slicing can perform the reversal internally.

# This approach can give better LeetCode runtime because slicing/reversed functions are optimized internally.

# Time Complexity: O(n)
# Space Complexity: O(n)

# What I Learned:

# I learned how to process strings in fixed-size blocks using step traversal.
# I understood how to apply the Two Pointer technique inside a specific range instead of the whole string.
# I also learned why min(start+k-1, len(s)-1) is used to handle the last incomplete block safely.

# CODE (Two Pointer Approach):

class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)

        for st in range(0, len(s), 2*k):
            l = st
            r = min(st+k-1, len(s)-1)

            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return "".join(s)
