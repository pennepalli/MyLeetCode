import sys


def is_valid_parentheses(s):
    """
    Checks if a string containing parentheses is valid.

    Args:
        s: The input string containing parentheses.

    Returns:
        True if the string is valid, False otherwise.
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:  # Closing bracket
            top_element = stack.pop() if stack else '#'  # Handle empty stack
            if mapping[char] != top_element:
                return False
        else:  # Opening bracket
            stack.append(char)
            # print ("Stack:", stack)

    return not stack  # Stack should be empty at the end


# Example Usage
print("():",is_valid_parentheses("()"))  # True
print("()[]{}:",is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("(]"))  # False
print(is_valid_parentheses("([)]"))  # False
print("{abcd[efgh]ijkl}:",is_valid_parentheses("{abcd[efgh]ijkl}"))  # True
print("{[({})]}:",is_valid_parentheses("{[({})]}"))  # True
print(is_valid_parentheses("")) # True (empty string is considered valid)
print(is_valid_parentheses("(")) # False (unclosed)
