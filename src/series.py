"""
    This module definces functions that implement mathematical series
"""


def fib(n):
    series = [0, 1]
    try:
        n = int(n)
    except:
        print(u'Please enter a valid integer.')
        return -2
    else:
        if n < 1:
            print(u'Please enter an integer greater than or equal to 1.')
            return -1
        while n > len(series):
            series.append(series[-1] + series[-2])
        return series[n - 1]


def fib_recursive(n, series=[0, 1]):
    """
    Return the nth value of the Fibonacci series, using a recursive approach.
    """
    try:
        n = int(n)
        series[0] = int(series[0])
        series[1] = int(series[1])
    except:
        print(u'Please enter a valid integer.')
        return -2
    else:
        if n < 1:
            print(u'Please enter an integer greater than or equal to 1.')
            return -1
        if n < len(series):
            return series[n - 1]
        else:
            series.append(series[-1] + series[-2])
            return fib_recursive(n, series)


def lucas(n):
    """Return the nth value of the Lucas series."""
    series = [2, 1]
    try:
        n = int(n)
    except:
        print(u'Please enter a valid integer.')
        return -2
    else:
        if n < 1:
            print(u'Please enter an integer greater than or equal to 1.')
            return -1
        while n > len(series):
            series.append(series[-1] + series[-2])
        return series[n - 1]


def sum_series(n, first=0, second=1):
    """
    Return the nth value of a custom sum series starting at 'first' and
    'second'.
    """
    series = [first, second]
    try:
        n = int(n)
        first = int(first)
        second = int(second)
    except:
        print(u'Please enter only valid integers.')
        return -2
    else:
        if n < 1:
            print(u'Please enter an integer greater than or equal to 1.')
            return -1
        while n > len(series):
            series.append(series[-1] + series[-2])
        return series[n - 1]

if __name__ == '__main__':
    print()
    print(u'This module definces functions that implement mathematical series')
    print()
    print(u'fib(n):')
    print(u'\tReturns the nth value in the fibonacci series.')
    print()
    print(u'>>> fibonacci(3) returns: {}'.format(fib(3)))
    print()
    print(u'fib_recursive(n):')
    print(u'\tReturns the nth value in the fibonacci series.')
    print()
    print(u'>>> fib_recursive(3) returns: {}'.format(fib_recursive(3)))
    print()
    print(u'lucas(n):')
    print(u'\tReturns the nth value in the lucas series.')
    print()
    print(u'>>> lucas(3) returns: {}'.format(lucas(3)))
    print()
    print(u'sum_series(n, s):')
    print(u'\tReturns the nth value in the series based on the entered seed value.')
    print()
    print(u'>>> sum_series(3, 2) returns: {}'.format(sum_series(3, 2)))
    print(u'which is the same as the lucas series')
    print()
