import pytest
from OOP import addition





def test_database(db_connection):
    print('running database')
    assert db_connection == 'data_base'

def test_session_add():
    assert addition


