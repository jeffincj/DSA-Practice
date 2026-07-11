# Problem NO: 27
# LeetCode: 121
# Problem: Best Time to Buy and Sell Stock
# Pattern: Greedy + Two Pointers (Single Pass)


# Brute Force:
# Try every possible pair of buying and selling days.
# For each buy day, check all later sell days.
# Calculate the profit for every pair.
# Return the maximum profit found.

# Time Complexity: O(n²)
# Space Complexity: O(1)


# Optimal Approach:
# Use Two Pointers to keep track of the best buying day and the current selling day.

# Initialize:
# Left pointer (l) as the buying day.
# Right pointer (r) as the selling day.

# If the selling price is higher than the buying price:
# Calculate the profit.
# Update the maximum profit if it is larger.

# Otherwise:
# Move the buying pointer to the current day because it has a lower price.

# Continue until all days are processed.

# Time Complexity: O(n)
# Space Complexity: O(1)


# What I Learned:
# I learned that the best buying price should always be the lowest price seen so far.
# Instead of checking every pair, I can update the buying day whenever I find a smaller price.
# The selling pointer keeps moving forward while the buying pointer only changes when a better buying opportunity appears.
# This reduces the time complexity from O(n²) to O(n).


# CODE:

class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r

            r += 1

        return max_profit
