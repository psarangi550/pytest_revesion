import pytest #importing the pytest module

@pytest.fixture(params=[(3,4),[3,5]],ids=["tup","list"])
def setup01(request):
    yield request.param
    del request.param

@pytest.fixture(params=["access","slice","assign"],ids=["access","slice","assign"])
def setup02(request):
    yield request.param
    del request.param
    

