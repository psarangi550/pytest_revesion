import pytest


#parameterizing the fixture in here 
@pytest.fixture(params=[10,20,30,40,50],ids=["args1","args2","args3","args4","args5"])
def setup(request):
    data=request.param
    yield data
    del data

#paramterizing with the help of list of tuples
@pytest.fixture(params=[(2,4),(3,27)],ids=["args1","args2"])
def setup01(request):
    yield request.param
    del request.param
    