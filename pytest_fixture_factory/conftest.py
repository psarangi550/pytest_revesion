import pytest

@pytest.fixture
def setup(request):
    def get_structure(name):
        if name=="list":
            return [1,2,3]
        elif name=="tuple":
            return (1,2,3)
    yield get_structure
    print("deleting the function object at the end")
    del get_structure
        