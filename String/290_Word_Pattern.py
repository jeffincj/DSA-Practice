# Problem NO: 22

# LeetCode: 290

# Problem: Word Pattern

# Pattern: HashMap + One-to-One Mapping


# Brute Force:
# Store the mapping from pattern character to word using a HashMap.
# To check whether another character is already mapped to the same word, search through all HashMap values.

# Time Complexity: O(n²)
# Space Complexity: O(n)


# Optimal Approach:
# Use two HashMaps to maintain a one-to-one relationship between pattern characters and words.

# Map 1:
# pattern character → word

# Map 2:
# word → pattern character

# While traversing:
# - If a pattern character already exists, check whether it maps to the same word.
# - If a word already exists, check whether it maps back to the same pattern character.
# - If both are new, create the mapping.

# This prevents two different characters from pointing to the same word.

# Time Complexity: O(n)
# Space Complexity: O(n)


# What I Learned:
# I learned how to solve one-to-one mapping problems using HashMaps.
# A single HashMap can check one direction, but two HashMaps are better when both sides must be unique.
# This pattern is useful when we need to maintain relationships like character-to-character or character-to-word mappings.


# CODE:

class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for p, w in zip(pattern, words):

            if p in p_to_w and p_to_w[p] != w:
                return False

            if w in w_to_p and w_to_p[w] != p:
                return False

            p_to_w[p] = w
            w_to_p[w] = p

        return True
