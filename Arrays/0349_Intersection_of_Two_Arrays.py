Problem NO: 5

# LeetCode: 349

# Problem: Intersection of Two Arrays

# Pattern: Array + HashSet

# Brute Force:
# Compare every element in the first array with every element in the second array. Store only the unique common elements.

# Time Complexity: O(n × m)

# Optimal Approach:
# Convert the first array into a HashSet. Traverse the second array and check whether each element exists in the HashSet. Store common elements in another HashSet to avoid duplicates.

# Time Complexity: O(n + m)

# Space Complexity: O(n + m)

# What I Learned:
# A HashSet provides O(1) average lookup time, making it efficient for checking whether an element exists. Using another HashSet automatically removes duplicate results while finding the intersection of two arrays.

# CODE:

class Solution(object):
    def intersection(self, nums1, nums2):
        s = set()
        si = set()

        for num in nums1:
            s.add(num)

        for num in nums2:
            if num in s:
                si.add(num)

        return list(si)
