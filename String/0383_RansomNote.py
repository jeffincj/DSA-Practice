# Problem NO: 21

# LeetCode: 383

# Problem: Ransom Note

# Pattern: HashMap + Frequency Counting

# Brute Force:
# For each character in ransomNote, search the character inside magazine.
# After finding the character, remove it from magazine to avoid using the same character again.

# Time Complexity: O(n*m)
# Space Complexity: O(n)


# Optimal Approach:
# Use a HashMap to store the frequency of each character from magazine.

# Step 1:
# Traverse magazine and count the occurrence of every character.

# Step 2:
# Traverse ransomNote and check whether each required character is available.

# Step 3:
# If the character count is 0 or the character is not available, return False.

# Step 4:
# Reduce the character count after using it.

# Time Complexity: O(n+m)
# Space Complexity: O(1)

# (where n = length of ransomNote, m = length of magazine)


# What I Learned:
# I learned how to solve character availability problems using HashMap frequency counting.
# Instead of repeatedly searching characters, we can store character counts first and use them when needed.
# I also learned that dictionary get() helps to check missing keys and values efficiently.


# CODE:

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}

        for ch in magazine:
            count[ch] = count.get(ch,0) + 1

        for ch in ransomNote:
            if count.get(ch,0) == 0:
                return False

            count[ch] -= 1

        return True
