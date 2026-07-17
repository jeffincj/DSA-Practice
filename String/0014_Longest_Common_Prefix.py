# Problem NO: 11

# LeetCode: 14

# Problem: Longest Common Prefix

# Pattern: Strings + String Traversal

# Brute Force:
# Compare every character of each string one by one until a mismatch is found.

# Time Complexity: O(n × m)

# Optimal Approach:
# Use the first string as a reference. Compare each character position with the corresponding character in every other string. Stop when a mismatch or the end of a string is reached.

# Time Complexity: O(n × m)

# Space Complexity: O(1)

# What I Learned:
# I learned how to compare multiple strings character by character using the first string as a reference. The comparison stops immediately when a mismatch or the end of any string is found, making the solution efficient.

# CODE:

class Solution(object):
    def longestCommonPrefix(self, strs): 
        res=""
        for i in range(len(strs[0])):
            for c in strs[1:]:
                if i==len(c) or c[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res