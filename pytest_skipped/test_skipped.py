import pytest
import sys
def cent_to_faren(cent=0):
    const=9/5
    far=(const*cent)+32
    return far

#skipping the whole test as below 
pytestmark=pytest.mark.skipif(sys.platform!='win32',reason="only run on the windows platform")

#Testing the function as below
# @pytest.mark.skip() #skipping without any reason 
def test_cent_to_faren1():
    assert cent_to_faren()==32

# @pytest.mark.skip(reason="skipping knowingly") #skipping with a reason
def test_cent_to_faren2():
    assert cent_to_faren()==32

#skipping with a condition and reason
# @pytest.mark.skipif(sys.platform!="win32",reason="skipping with a condition")
def test_cent_to_faren3():
    assert cent_to_faren(38)==100.4
    
# #skipping with a condition but no reason
# @pytest.mark.skipif(sys.platform!="win32")
# def test_cent_to_faren3():
#     assert cent_to_faren(38)==100.4
