def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def generic_sequence(n, s):
    if n == 0:
        return s
    elif n == 1:
        return 1
    return generic_sequence(n - 1, s) + generic_sequence(n - 2, s)
