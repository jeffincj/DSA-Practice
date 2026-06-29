# Problem NO: 9

# LeetCode: 125

# Problem: Valid Palindrome

# Pattern: Strings + Two Pointers

# Brute Force:
# Create a new string containing only lowercase alphanumeric characters and compare it with its reverse.

# Time Complexity: O(n)

# Space Complexity: O(n)

# Optimal Approach:
# Use two pointers from both ends of the string. Skip non-alphanumeric characters and compare lowercase characters directly without creating a new string.

# Time Complexity: O(n)

# Space Complexity: O(1)

# What I Learned:
# Two pointers can compare characters from both ends while skipping unwanted characters. This avoids creating a new string and reduces the extra space from O(n) to O(1).

# CODE:

class Solution(object):
    def isPalindrome(self, s):
        l,r=0,len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1,r-1
        return True


            
