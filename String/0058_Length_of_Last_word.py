# Problem NO: 12

# LeetCode: 58

# Problem: Length of Last Word

# Pattern: Strings + Reverse Traversal

# Brute Force:
# Split the string into words and return the length of the last word.

# Time Complexity: O(n)

# Space Complexity: O(n)

# Optimal Approach:
# Traverse the string from right to left. Skip trailing spaces, then count characters until another space or the beginning of the string is reached.

# Time Complexity: O(n)

# Space Complexity: O(1)

# What I Learned:
# Instead of storing every word, I can traverse the string from the end and count only the characters of the last word. This reduces the extra space from O(n) to O(1).

# CODE:

class Solution(object):
    def lengthOfLastWord(self, s):
        i= len(s)-1
        while i>=0 and s[i]==" ":
            i-=1
        l=0
        while i>=0 and s[i]!=" ":
            l+=1
            i-=1
        return l
