# Problem NO: 6

# LeetCode: 202

# Problem: Happy Number

# Pattern: HashSet + Cycle Detection

# Brute Force:
# Keep calculating the sum of the squares of digits until the number becomes 1 or starts repeating.

# Time Complexity: O(log n)

# Optimal Approach:
# Use a HashSet to store every intermediate number. If the number becomes 1, it is a happy number. If a number repeats, a cycle is detected, so return False.

# Time Complexity: O(log n)

# Space Complexity: O(log n)

# What I Learned:
# A HashSet can be used to detect cycles by storing previously seen values. If the same value appears again, the process is repeating and will never reach 1.



#CODE:

class Solution(object):
    def isHappy(self, n,seen=None):
        if seen is None: seen=set()
        s=0
        while n!=0:
            d=n%10
            s=s+d*d
            n=n//10
        if s==1: return True
        if s in seen:return False
        seen.add(s)
        return self.isHappy(s,seen)
