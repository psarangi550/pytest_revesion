import string
import pytest
import sys 

@pytest.mark.xfail(raises=IndexError,reason="expecting an IndexError Exception")
def test_check():
    assert string.ascii_lowercase[100] == "a"

#here checking in this case what will be response
@pytest.mark.xfail(raises=IndexError,reason="expecting an IndexError Exception")
def test_check01():
    assert string.ascii_lowercase[0] == "a"

#here using the xfail with the sys module as 
@pytest.mark.xfail(sys.platform=="linux",reason="works on windows system only")
def test_check02():
    assert string.ascii_lowercase[100] == "a"

#but if the condition does not match and test got poassed then we will get the XPASSED as status
@pytest.mark.xfail(sys.platform=="win32",reason="Running the Test to make it as xpassed")
def test_check03():
    assert string.ascii_lowercase[-1] == "z"
    