# -*- coding: utf-8 -*-
import pytest

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


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fib(n, result):
    from fib import fib
    assert fib(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    from fib import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_generic_sequence_fib(n, result):
    from fib import generic_sequence
    assert generic_sequence(n, 0) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_generic_sequence_lucas(n, result):
    from fib import generic_sequence
    assert generic_sequence(n, 2) == result
