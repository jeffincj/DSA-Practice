# Problem NO: 25

# LeetCode: 15

# Problem: 3Sum

# Pattern: Sorting + Two Pointers + Duplicate Handling


# Brute Force:
# Use three loops and check every possible triplet.
# If the sum of three numbers is zero, add the triplet.

# Time Complexity: O(n³)
# Space Complexity: O(n)


# Optimal Approach:
# First sort the array.
# Fix one number using a loop and convert the remaining problem into a Two Sum problem.
# Use two pointers (left and right) to find the remaining two numbers.

# If the total sum is smaller than zero, move the left pointer to increase the sum.
# If the total sum is greater than zero, move the right pointer to decrease the sum.
# If the total is zero, store the triplet and skip duplicate values.

# Time Complexity: O(n²)
# Space Complexity: O(1)


# What I Learned:
# I learned how to solve a three-value problem by reducing it into a two-value problem.
# Instead of searching for three numbers together, fix one number and use the Two Pointer technique for the remaining array.

# I also learned why sorting helps:
# - It allows pointer movement based on sum value.
# - It helps remove duplicate triplets easily.

# Whenever a problem asks for combinations of multiple numbers:
# 3Sum → Fix one number + Two Pointer
# 4Sum → Fix two numbers + Two Pointer


# CODE:

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif total < 0:
                    l += 1

                else:
                    r -= 1

        return ans
