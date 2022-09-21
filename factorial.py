# This program uses recursion to calculate
# the factorial of a number.

# The factorial function uses recursion to
# calculate the factorial of its argument,
# which is assumed to be nonnegative.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

    
if __name__ == "__main__":
    import sys
    factorial(int(sys.argv[1]))
