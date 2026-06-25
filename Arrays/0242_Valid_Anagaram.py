# Problem NO: 4

# LeetCode: 242

# Problem: Valid Anagram

# Pattern: String + HashMap + Frequency Counting

# Brute Force:
# Sort both strings and compare them.

# Time Complexity: O(n log n)

# Optimal Approach:
# Use a HashMap to count the frequency of each character in the first string. Traverse the second string and decrease the corresponding frequency. If all frequencies become zero, the strings are anagrams.

# Time Complexity: O(n)

# Space Complexity: O(n)

# What I Learned:
# A HashMap can efficiently store the frequency of characters. By increasing counts for one string and decreasing them for the other, I can verify whether both strings contain the same characters with the same frequency in O(n) time.

#CODE:
class Solution(object):
    def isAnagram(self, s, t):
        f={}
        for c in s:
            if c in f:f[c]+=1
            else :f[c]=1
        for c in t:
            if c not in f:return False
            elif f[c]==1:del f[c]
            else:f[c]-=1
        return not f
