# LeetCode 20 - Valid Parentheses

## Problem
Given a string `s` containing the characters:
- `(`
- `)`
- `{`
- `}`
- `[`
- `]`

Determine if the input string is valid.

A string is valid if:
- Every opening bracket has a corresponding closing bracket.
- Brackets are closed in the correct order.
- Every closing bracket matches the most recent unmatched opening bracket.

---

## Approach

This solution uses a **Stack**.

### Steps
1. Create a dictionary to map each closing bracket to its opening bracket.
2. Traverse each character in the string.
3. If it is an opening bracket, push it onto the stack.
4. If it is a closing bracket:
   - Check if the stack is empty.
   - Check whether the top of the stack matches the corresponding opening bracket.
   - If not, return `False`.
5. Remove the matched opening bracket from the stack.
6. After processing all characters, return `True` only if the stack is empty.

---

## Time Complexity

- **O(n)**

---

## Space Complexity

- **O(n)**

---

## Python Code

```python
class Solution(object):
    def isValid(self, s):
        pair = {')':'(', ']':'[', '}':'{'}
        st = []

        for i in s:
            if i in '({[':
                st.append(i)
            else:
                if not st or pair[i] != st[-1]:
                    return False
                st.pop()

        return not st
```

---

## Concepts Used

- Stack
- Dictionary (Hash Map)
- String Traversal

---

## What I Learned

- How stacks solve bracket matching problems.
- Using a dictionary makes matching brackets simple.
- Checking the top element of the stack before popping avoids errors.
