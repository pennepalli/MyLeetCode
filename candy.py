#!/usr/bin/python3

import sys

def candy(ratings):
    n = len(ratings)
    candies = [1] * n  # Step 1: Give each child at least 1 candy

    # Step 2: Left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Step 3: Right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    print(candies)
    return sum(candies)
if __name__ == "__main__":
    inarr = [int(num) for num in sys.argv[1].split(",")]
    print(inarr)
    print(candy(inarr))
