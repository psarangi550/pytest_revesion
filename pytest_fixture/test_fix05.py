import pytest #importing the pytest module
import os
import csv
@pytest.fixture
def setUp(request):
    file_obj=open("/mnt/c/Users/611903295/Downloads/pytest_revesion/pytest_fixture/emp.csv","r")
    yield file_obj
    file_obj.close()
    os.remove("/mnt/c/Users/611903295/Downloads/pytest_revesion/pytest_fixture/emp.csv")

def test_file_read(setUp):
    csv_reader=csv.reader(setUp)
    next(csv_reader)
    for line in csv_reader:
        print(line)
    assert True
    
    
