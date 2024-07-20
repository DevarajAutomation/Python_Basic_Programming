"""Conftest.py"""

import pytest

@pytest.fixture()
def db_connection():

    print("The database is loading")
    connection="data_base"
    yield connection

    print('Teardown')
    connection=None

