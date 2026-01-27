class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Key must be the CLOSING bracket for the logic to work
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Pop the top of stack or use dummy '#' if stack is empty
                top_element = stack.pop() if stack else '#'
                # Check if the opening bracket matches
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push to stack
                stack.append(char)
        
        return not stack
