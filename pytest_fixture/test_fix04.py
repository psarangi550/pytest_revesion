import pytest

weekday1=["mon","tue","wed"]
weekday2=["fri","sat","sun"]


@pytest.fixture()
def setUp():
    weekday1.append("thr")
    yield weekday1
    weekday1.pop()

@pytest.fixture()
def setUp01():
    weekday2.insert(0,"thr")
    yield weekday2
    weekday2.remove("thr")
def test_foo(setUp,setUp01):
    assert len(setUp)==len(setUp01) 

def test_foo2(setUp):
    print(setUp)
    setUp.extend(weekday2)
    print(setUp)
    assert len(setUp)==len(["mon","tue","wed","thr","fri","sat","sun"])


     
    
