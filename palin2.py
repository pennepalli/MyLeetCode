import sys

def is_palindrome(text):
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    Handles unicode correctly.

    Args:
        text: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    processed_text = ''.join(c.lower() for c in text if c.isalnum())
    return processed_text == processed_text[::-1]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <string>")
        sys.exit(1)

    input_string = sys.argv[1]
    print(f"Input string: {input_string}")

    if is_palindrome(input_string):
        print(f"'{input_string}' is a palindrome")
    else:
        print(f"'{input_string}' is not a palindrome")

    sys.exit(0)
