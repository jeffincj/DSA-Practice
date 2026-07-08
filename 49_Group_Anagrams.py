# Problem NO: 23

# LeetCode: 49

# Problem: Group Anagrams

# Difficulty: Medium

# Pattern: HashMap + Sorting as Key


# Brute Force:
# Compare every string with every other string and check whether they are anagrams.
# Group the matching words together.

# Time Complexity: O(n² * k log k)
# Space Complexity: O(n*k)


# Optimal Approach:
# Use a HashMap to group words.

# Observation:
# Anagrams will become the same string after sorting.

# Example:

# eat → aet
# tea → aet
# ate → aet

# All have the same key, so store them in the same group.

# Steps:
# 1. Create an empty HashMap.
# 2. Traverse each word in the list.
# 3. Sort the characters of the word to create a unique key.
# 4. Store the original word in the HashMap using that key.
# 5. Return all HashMap values.

# Time Complexity: O(n * k log k)

# n = number of words
# k = average length of each word

# Space Complexity: O(n*k)


# What I Learned:
# I learned how to use a common identity as a HashMap key.
# Instead of comparing every pair of strings, convert each anagram into the same sorted form and group them together.
# This introduced the HashMap grouping pattern, which is useful for many medium-level problems.


# CODE:

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
