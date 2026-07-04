# Problem NO: 16

# LeetCode: 242

# Problem: Valid Anagram

# Pattern: String + HashMap + Frequency Counting

# Brute Force:

# Sort both strings and compare them.

# If both sorted strings are equal, then both strings contain the same characters with the same frequency.

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Optimal Approach:

# Use a HashMap to store the frequency count of each character.

# Steps:

# First check if both string lengths are equal
# Traverse the first string and count every character
# Traverse the second string and decrease the character count
# If any character is missing, return False
# Remove characters when their count becomes zero
# If the HashMap becomes empty, both strings are anagrams

# Time Complexity: O(n)
# Space Complexity: O(1)

# What I Learned:

# I learned how to use HashMap for character frequency counting.
# Instead of comparing characters one by one, storing the count makes checking easier.
# I also learned how .get() helps update dictionary values without writing extra conditions.

# This pattern is useful for many string problems involving character comparison.

# CODE:

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False

            count[ch] -= 1

            if count[ch] == 0:
                del count[ch]

        return len(count) == 0
