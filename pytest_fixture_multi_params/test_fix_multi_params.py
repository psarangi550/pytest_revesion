import pytest 

@pytest.mark.xfail(raises=TypeError,reason="known issue as tuple is immutable")
def test_foo(setup01,setup02):
    print(setup01)
    print(setup02)
    if setup02=="access":
        print(setup01[0])
        assert setup01[0]
    elif setup02=="slice":
        print(setup01[::-1])
        assert setup01[::-1]
    elif setup02=="assign":
        setup01[1]=99
        assert True