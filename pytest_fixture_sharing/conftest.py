import pytest
import sqlite3

#opening the sqlite db using the fixture in the conftest.py file 
@pytest.fixture(scope="function")
def set_up(request):
    conn=sqlite3.connect(":memory:")
    cursor=conn.cursor()
    yield cursor
    cursor.close()
    conn.close()
    
    