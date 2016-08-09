"""
    This module definces functions that implement mathematical series
"""


def fib(n):
    if type(n) != int:
        return 'This is not an integer'
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

if __name__ == '__main__':
    print()
    print(u'This module definces functions that implement mathematical series.')
    print()
    print(u'fibonacci(n):')
    print(u'\tReturns the nth value in the fibonacci series.')
    print()
    print(u'>>> fibonacci(3) returns: {}'.format(fib(3)))
    print()
    print(u'lucas(n):')
    print(u'\tReturns the nth value in the lucas series.')
    print()
    print(u'>>> lucas(3) returns: {}'.format(lucas(3)))
    print()
    print(u'generic_sequence(n):')
    print(u'\tReturns the nth value in the series based on the entered seed value.')
    print()
    print(u'>>> generic_sequence(3, 2) returns: {}'.format(generic_sequence(3,2)))
    print(u'which is the same as the lucas series')
    print()
