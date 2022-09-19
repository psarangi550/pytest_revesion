import pytest #importing the pytest module in here

def pytest_addoption(parser):
    parser.addoption("--env",default="dev",help="provide environment")
    
@pytest.fixture
def setup(pytestconfig):#using the pytestconfig fixture here
    env_val=pytestconfig.getoption("env")
    if env_val=="dev":
        file_obj=open("/mnt/c/Users/611903295/Downloads/pytest_revesion/pytest_cmd_args_passing/dev.prop","r")
    elif env_val=="uat":
        file_obj=open("/mnt/c/Users/611903295/Downloads/pytest_revesion/pytest_cmd_args_passing/qa.prop","r")
    else:
        file_obj=open("/mnt/c/Users/611903295/Downloads/pytest_revesion/pytest_cmd_args_passing/prod.prop","r")
    yield file_obj
    file_obj.close()
    
    
        
        