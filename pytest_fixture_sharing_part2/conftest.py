import pytest

def pytest_configure():
    pytest.weekday1=["mon","tue","wed"]
    pytest.weekday2=["fri","sat","sun"]
    
@pytest.fixture(scope="function")
def setUp(request):
    weekday1=pytest.weekday1
    weekday1.append("thr")
    yield weekday1
    weekday1.pop()
    
    