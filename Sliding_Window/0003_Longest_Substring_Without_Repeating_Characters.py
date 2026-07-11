# Problem NO: 28
# LeetCode: 3
# Problem: Longest Substring Without Repeating Characters
# Pattern: Sliding Window + Hash Set

# Brute Force:
# Check every possible substring.
# For each substring, verify whether all characters are unique.
# Keep track of the maximum valid substring length.

# Time Complexity: O(n²)
# Space Complexity: O(n)


# Optimal Approach:
# Use a Sliding Window with a Hash Set.

# Maintain two pointers:
# - Left pointer (l) marks the start of the current window.
# - Right pointer (r) expands the window one character at a time.

# If the current character already exists in the window:
# Remove characters from the left side until the duplicate is removed.

# Add the current character to the set.
# Update the maximum window length using:
# r - l + 1

# Time Complexity: O(n)
# Space Complexity: O(min(n, alphabet size))


# What I Learned:
# I learned the standard Sliding Window template.
# A Hash Set allows O(1) duplicate checking.
# When a duplicate appears, shrink the window instead of restarting.
# The window length is always calculated as:
# r - l + 1
# This Sliding Window pattern is reusable for many substring problems.


# CODE:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        m = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            m = max(m, r - l + 1)

        return m
