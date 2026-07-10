# Problem NO: 26

# LeetCode: 11

# Problem: Container With Most Water

# Pattern: Two Pointers


# Brute Force:
# Check every possible pair of lines using nested loops.
# For every pair, calculate the water area and store the maximum area.

# Formula:
# Area = width × minimum height

# Time Complexity: O(n²)
# Space Complexity: O(1)


# Optimal Approach:
# Use the Two Pointer technique.

# Place one pointer at the beginning and another pointer at the end.
# Calculate the current container area using the smaller height.

# Update the maximum area whenever a larger area is found.

# Move the pointer with the smaller height because the smaller line limits the water capacity.
# Moving the taller line cannot increase the area since width decreases.

# Continue until both pointers meet.

# Time Complexity: O(n)
# Space Complexity: O(1)


# What I Learned:
# I learned how to optimize a problem from checking all pairs to using the Two Pointer approach.
# I understood that the container capacity depends on the smaller height.
# By moving the smaller pointer, we search for a taller line that can increase the maximum area.


# CODE:
class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:

            if height[l] < height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1

            if area > maxArea:
                maxArea = area

        return maxArea
