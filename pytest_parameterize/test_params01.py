import pytest 
# from math import product
from functools import reduce

@pytest.mark.parametrize('input', [10,20,30,40])
def test_foo1(input):
    assert type(input)==int

@pytest.mark.parametrize('input,output', [(2,4),(3,27),(4,256)])
def test_foo2(input,output):
    assert input**input==output
    
#here using the parameter with the condition as below 
data_set=[
    ([2,3,4],"sum",9),
    ([2,3,4],"mul",24)
]

@pytest.mark.parametrize('a,b,c', data_set)
def test_foo3(a,b,c):
    if b=="sum":
        assert sum(a)==c
    elif b=="mul":
        assert reduce(lambda x,y:x*y,a)==c
    else:
        assert False
