from OOP import test

import pytest


def test_add():
    assert test.sum_two(2, 3) == 5


@pytest.mark.parametrize("a,b,expected", [(3, 4,7), (8, 9,15), (9, 11,20)])
def test_two_three(a, b, expected):
    assert test.sum_two(a, b) == expected
