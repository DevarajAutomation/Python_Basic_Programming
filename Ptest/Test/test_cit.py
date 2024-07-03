from Pytest.devel.project import Point


def test_hello():
    p1=Point()

    assert p1.greet_user('dev')