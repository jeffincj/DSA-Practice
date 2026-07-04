# Problem NO: 15

# LeetCode: 151

# Problem: Reverse Words in a String

# Pattern: String Traversal + Two Pointers + Word Reversal

# Brute Force:
# Split the string into words, create another list, insert words in reverse order, and join them.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimal Approach:
# First remove extra spaces and separate words using split().
# Then apply the Two Pointer technique:
# Left pointer starts at the first word
# Right pointer starts at the last word
# Swap both words
# Move both pointers toward the center

# Finally join the list back into a string.
# Time Complexity: O(n)
# Space Complexity: O(n)

# What I Learned:
# I learned how to reverse the order of words in a sentence using Two Pointers.
# I understood that split() automatically handles multiple spaces and creates a clean list of words.
# I practiced reversing elements inside a list without using built-in reverse functions.

# CODE:

class Solution(object):
    def reverseWords(self, s):
        s = s.split()

        l = 0
        r = len(s)-1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return " ".join(s)
