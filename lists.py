
import sys


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("my_list: ",  my_list)

print("my_list[2:5] : ", my_list[2:5]) # Extracts elements from index 2 (inclusive) up to index 5 (exclusive). Result: [2, 3, 4]

print ("my_list[:5] : ", my_list[:5]) # Extracts elements from the beginning of the list up to index 5 (exclusive). (Omitting start defaults to 0). Result: [0, 1, 2, 3, 4]
print ("Reverse my_list[::-1] : ", my_list[::-1]) # Reverses the entire list. Result: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#  my_list[5:] # Extracts elements from index 5 (inclusive) to the end of the list. (Omitting stop defaults to the end). Result: [5, 6, 7, 8, 9]

#  my_list[:] # Creates a complete copy of the list. (Omitting both start and stop creates a slice of the entire sequence). Result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#  my_list[2:8:2] # Extracts elements from index 2 up to 8, but takes every second element. Result: [2, 4, 6]

#  Negative Steps (Reversing and More):


#  my_list[5::-1] # Extracts elements from index 5 to the beginning, reversing the order. Result: [5, 4, 3, 2, 1, 0]

#  my_list[5:2:-1] # Extracts elements from index 5 down to (but not including) index 2, reversing the order. Result: [5, 4, 3]

#  my_list[2:5:-1] # Returns an empty list. Because the start index (2) is less than the stop index (5), and the step is -1 (negative), the slice cannot be constructed. There is nothing to return, so it returns empty []

"""
my_string = "Hello, World!"
Use code with caution.
Python
my_string[7:12] : Extracts "World".

my_string[:5] : Extracts "Hello".

my_string[-6:] : Extracts "World!". Negative indices count from the end of the string.

my_string[::-1] : Reverses the string: "!dlroW ,olleH"

my_string[::2] : Extracts every second character: "Hlo ol!"

More Complex Examples:

my_list[-1:2:-1] : Starts at the last element, goes down to (but does not include) index 2, decrementing by 1 each time. Result: [9, 8, 7, 6, 5, 4, 3]

my_string[1::2] : Starts at index 1, goes to the end, skipping every other character. Result: "el, ol!"

Important Notes:

stop Index is Exclusive: The stop index is not included in the slice.

Defaults:

If start is omitted, it defaults to 0 (the beginning).

If stop is omitted, it defaults to the end of the sequence.

If step is omitted, it defaults to 1.

Out-of-Bounds Indices: If start or stop are out of range, Python handles it gracefully. The slice will include elements up to the valid boundary.

Empty Slices: If the start, stop, and step values result in a logically impossible slice (e.g., trying to go forward with a negative step), you'll get an empty slice (e.g., [] or "").
"""
