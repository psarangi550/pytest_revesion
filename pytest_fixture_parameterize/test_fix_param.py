def test_foo(setup):
    assert type(setup)==int

def test_foo1(setup01):
    print(setup01)
    assert setup01[0]**setup01[0] == setup01[1]