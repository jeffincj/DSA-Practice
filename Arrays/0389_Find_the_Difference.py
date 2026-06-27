# Problem NO: 7

# LeetCode: 389

# Problem: Find the Difference

# Pattern: String + HashMap + Frequency Counting

# Brute Force:
# Compare the frequency of every character in both strings and find the extra character.

# Time Complexity: O(n²)

# Optimal Approach:
# Use a HashMap to count the frequency of characters in the first string. Traverse the second string and decrease the frequency. If a character is not found or its frequency becomes zero, that character is the extra one.

# Time Complexity: O(n)

# Space Complexity: O(n)

# What I Learned:
# Frequency counting using a HashMap can efficiently compare two strings. By increasing counts for one string and decreasing them for the other, the extra character can be found in linear time.

# CODE:
class Solution(object):
    def findTheDifference(self, s, t):
        d={}
        for char in s:
            if char in d: d[char]+=1
            else: d[char]=1
        for char in t:
            if char not in d or d[char]==0: return char
            else: d[char]-=1                                                                                                                        
