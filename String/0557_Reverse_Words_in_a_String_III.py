# Problem NO: 13

# LeetCode: 557

# Problem: Reverse Words in a String III

# Pattern: String Traversal + Reverse While Building

# Brute Force:
# Traverse the string, build each word, reverse it, and append it to the result.

# Time Complexity: O(n)

# Space Complexity: O(n)

# Optimal Approach:
# Traverse the string character by character. Build each word in reverse by adding the current character to the front of a temporary string. When a space is encountered, append the reversed word to the result and continue until the end of the string.

# Time Complexity: O(n)

# Space Complexity: O(n)

# Alternative Approach:
# Convert the string into a list of characters and reverse each word using the Two Pointers technique.

# What I Learned:
# I learned how to identify word boundaries while traversing a string. By adding each character to the front of a temporary string, I can reverse each word without calling a separate reverse function. I also learned another approach using Two Pointers to reverse each word in place.

# CODE:
class Solution(object):
    def reverseWords(self, s):
        rs = ""
        ch = ""

        for c in s:
            if c != " ":
                ch = c + ch
                continue
            else:
                ch += " "
                rs += ch
                ch = ""

        return rs + ch
