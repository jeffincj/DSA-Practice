# Problem: Contains Duplicate

# LeetCode: 217

# Pattern: Array + Hashing

# Brute Force: Store visited elements in a list and check membership using 'in'.

# Time Complexity: O(n²)

# Optimal Approach: Use a HashSet to track seen elements or compare len(set(nums)) with len(nums).

# Time Complexity: O(n)

# Space Complexity: O(n)

# What I Learned: A list takes O(n) time to search for an element, while a set uses hashing and provides O(1) average lookup time. Using a set reduces the overall complexity from O(n²) to O(n).

#CODE:

class Solution(object):
    def containsDuplicate(self, nums):
        return(len(set(nums))!=len(nums))
