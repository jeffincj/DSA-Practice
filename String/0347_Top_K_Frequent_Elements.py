# Problem NO: 24

# LeetCode: 347

# Problem: Top K Frequent Elements

# Pattern: HashMap + Frequency Counting + Sorting

# Brute Force:
# For every element, count how many times it appears by scanning the array repeatedly.
# After finding frequencies, choose the top k frequent elements.

# Time Complexity: O(n²)
# Space Complexity: O(n)


# Optimal Approach 1:
# Use a HashMap to store the frequency of each number.
# Sort the dictionary items based on frequency in descending order.
# Return the first k elements.

# Time Complexity: O(n log n)
# Space Complexity: O(n)


# More Optimized Approach:
# Use Bucket Sort.
# Create buckets based on frequency because maximum frequency cannot exceed array length.
# Traverse buckets from highest frequency to lowest and collect k elements.

# Time Complexity: O(n)
# Space Complexity: O(n)


# What I Learned:
# I learned how to use HashMap for frequency counting.
# When a problem asks for "most frequent", "top k", or "highest occurrence",
# first count the frequency using a dictionary.
# I also learned that sorting works but Bucket Sort can improve the time complexity.


# CODE:
class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}

        for n in nums:
            d[n] = d.get(n,0) + 1

        out = [
            key for key,value in 
            sorted(d.items(), key=lambda x:x[1], reverse=True)
        ]

        return out[:k]
