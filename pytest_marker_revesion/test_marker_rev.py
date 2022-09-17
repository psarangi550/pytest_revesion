import string
import pytest

#on the module level also we can declare this as below 
pytestmark=[pytest.mark.smoke,pytest.mark.strtest]

@pytest.mark.run(order=2)
@pytest.mark.smoke
def test_check01():
    assert str.upper(string.ascii_lowercase)==string.ascii_uppercase

@pytest.mark.run(order=3)
@pytest.mark.smoke
def test_check02():
    assert string.ascii_lowercase[-1]=="z"

@pytest.mark.run(order=1)
@pytest.mark.smoke
@pytest.mark.strtest
def test_check03():
    assert " ".join(["python","is","great"])=="python is great"