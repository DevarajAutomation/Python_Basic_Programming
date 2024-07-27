import pytest


def valid_age(age):
    if isinstance(age, int) and 18 <= age <= 60:
        return True
    return False


@pytest.mark.parametrize("age accepted", [
    (25, True),
    (17, False),
    (65, False)])
def test_valid_age(age):
    assert valid_age(98)
