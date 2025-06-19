# In a for or while loop the break statement may be paired with an else clause. If the loop finishes without executing the break, the else clause executes.

# In a for loop, the else clause is executed after the loop finishes its final iteration, that is, if no break occurred.

# In a while loop, it’s executed after the loop’s condition becomes false.

# In either kind of loop, the else clause is not executed if the loop was terminated by a break.
#  Of course, other ways of ending the loop early, such as a return or a raised exception, will also skip execution of the else clause.


for n in range(2, 1000):
    for x in range(2, n):
        if n % x == 0:
            # print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# (Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement.)

# One way to think of the else clause is to imagine it paired with the if inside the loop.
#     As the loop executes, it will run a sequence like if/if/if/else.
#     The if is inside the loop, encountered a number of times.
#     If the condition is ever true, a break will happen.
#     If the condition is never true, the else clause outside the loop will execute.

# When used with a loop, the else clause has more in common with the else clause of a try statement
#    than it does with that of if statements: a try statement’s else clause runs when no exception occurs
#    and a loop’s else clause runs when no break occurs. For more on the try statement and exceptions, see Handling Exceptions.
