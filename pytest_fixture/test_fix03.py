import pytest

@pytest.fixture(scope="class")
def setup(request):
    cities=["dehli","mumbai","karnataka","odisha"]
    request.cls.cities=cities
    yield cities
    del cities

@pytest.mark.usefixtures("setup")
class TestFoo01():
    
    def test_usage(cls):
        print(cls.cities)
        assert 1