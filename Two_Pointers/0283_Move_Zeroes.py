# Problem NO: 26
# LeetCode: 283
# Problem: Move Zeroes
# Pattern: Two Pointers (Fast & Slow Pointer)

# Brute Force:
# Create another array and store all non-zero elements first.
# After that, add all zeroes at the end.
# Copy the result back to the original array.

# Time Complexity: O(n)
# Space Complexity: O(n)


# Optimal Approach:
# Use Two Pointers to move all non-zero elements forward in-place.

# Use one pointer to scan the array.
# Use another pointer to track the correct position for the next non-zero element.

# When a non-zero number is found:
# Swap it with the position pointer and move the position pointer forward.

# This keeps all non-zero elements at the beginning and automatically moves zeroes to the end.

# Time Complexity: O(n)
# Space Complexity: O(1)


# What I Learned:
# I learned how to use the Fast & Slow Pointer technique.
# When a problem asks to modify an array in-place, avoid creating a new array.
# One pointer can search elements while another pointer maintains the correct position.


# CODE:

class Solution(object):
    def moveZeroes(self, nums):
        c = 0
        l = 0
        r = len(nums)

        while l < r:
            if nums[l] != 0:
                nums[c], nums[l] = nums[l], nums[c]
                c += 1

            l += 1
