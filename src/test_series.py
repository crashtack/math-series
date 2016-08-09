# -*- coding: utf-8 -*-
import pytest

def import_class(modulename, classname):
    ''' Returns imported class. '''
    try:
        return getattr(__import__(modulename, globals(), locals(), [classname], -1), classname)
    except AttributeError:
        print 'Error in importing class. "%s" has no class "%s"' % (modulename, classname)
        return None
    except ImportError as e:
        print 'Error in importing class: %s' % (e)
        return None

FIB_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21)
]

LUCAS_TABLE = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
    (7, 29),
    (8, 47)
]

PARAM_TABLE = [
    ('fib', 'Hello', 'This is not an integer'),
    ('lucas', 'Hello', 'This is not an integer'),
    ('generic_sequence', 'Hello', 'This is not an integer')
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fib(n, result):
    from series import fib
    assert fib(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_generic_sequence_fib(n, result):
    from series import generic_sequence
    assert generic_sequence(n, 0) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_generic_sequence_lucas(n, result):
    from series import generic_sequence
    assert generic_sequence(n, 2) == result


@pytest.mark.parametrize('func, test, response', PARAM_TABLE)
def test_input_type(func, test, response):
    from series import func
    assert func(test) == response


def test_lucas_input_type():
    from series import lucas
    assert lucas('hello') == 'This is not an integer'


def test_generic_sequence_input_type():
    from series import generic_sequence
    assert generic_sequence('hello', 'hello') == 'This is not an integer'
