import pytest # importing the pytest module 

@pytest.fixture(scope="function")
def setup_func():
    cities=["poland","swizerland","denmark","iceland"]
    return cities

#here using the fixture in the test function as below 
def test_foo(setup_func):#test function with setup_func fixture on function level
    assert len(setup_func)==4
    assert setup_func[0]=="poland"
    
