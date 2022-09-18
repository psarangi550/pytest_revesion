import pytest #importing the pytest module
@pytest.fixture
def setup(request):
    cities=["karnataka","odisha","mumbai","dehli"]
    yield cities
    del cities

def test_foo1(setup):
    assert len(setup)==4
    assert setup[0]=="karnataka"