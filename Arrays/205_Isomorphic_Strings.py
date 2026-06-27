Problem NO: 8

LeetCode: 205

# Problem: Isomorphic Strings

# Pattern: String + HashMap + Character Mapping

# Brute Force:
# Compare each character with every other character and verify that each character maps consistently without conflicts.
# Time Complexity: O(n²)

# Optimal Approach:
# Use a HashMap to map characters from one string to another. Ensure each character always maps to the same character and that no two different characters map to the same target character.
# Time Complexity: O(n)
# Space Complexity: O(n)

# What I Learned:
# A HashMap can be used to maintain one-to-one character mappings. Besides checking if a character has been mapped before, I also need to ensure that no two different characters map to the same character.

# CODE: 
class Solution(object):
    def isIsomorphic(self, s, t):
        c={}
        n=0
        if len(s)==len(t):
            for i , char in enumerate(t):
                if char in c:
                    if c[char] ==s[i]:
                        n+=1
                    else:
                        return False
                elif s[i] not in c.values():
                    c[char]=s[i]
                    n+=1
                else:
                    return False
            if n==len(s):
                return True      

