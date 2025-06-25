#!/usr/bin/python3

import itertools
import operator

# List of numbers
numbers = [2, 3, 6, 8, 12, 60]
target = 327

# Allowed operators and their functions
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# Generate all binary expressions with a list of numbers and operations
def generate_exprs(nums):
    if len(nums) == 1:
        yield str(nums[0])
    else:
        for i in range(1, len(nums)):
            left = nums[:i]
            right = nums[i:]
            for l in generate_exprs(left):
                for r in generate_exprs(right):
                    for op in ops:
                        expr = f'({l}{op}{r})'
                        yield expr

# Try all permutations of length 2 to 6
results = set()
for n in range(2, len(numbers)+1):
    for subset in itertools.permutations(numbers, n):
        for expr in generate_exprs(list(subset)):
            try:
                val = eval(expr)
                if abs(val - target) < 1e-9:
                    results.add(expr)
            except ZeroDivisionError:
                continue

# Display results
print(f"Expressions that evaluate to {target}:")
for expr in sorted(results):
    print(expr)

