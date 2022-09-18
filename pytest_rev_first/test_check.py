import sys

def test_check():
    assert 5 + 5 == 10, "Test Passed"


def test_check1():
    assert 5 * 5 == 25, "failed Test Intentionally"

# def test_syscheck():
#     assert (sys.version_info.major,sys.version_info.minor)==(3,7)
#     assert 1