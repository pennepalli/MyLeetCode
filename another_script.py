import palindrome_checker

my_string = "Racecar"
if palindrome_checker.is_palindrome(my_string):
    print(f"'{my_string}' is a palindrome (checked by another_script.py)")
else:
    print(f"'{my_string}' is not a palindrome (checked by another_script.py)")
