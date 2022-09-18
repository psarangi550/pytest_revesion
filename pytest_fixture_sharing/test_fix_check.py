def test_db_connection(set_up):
    set_up.execute("create table EMP (eno Integer,ename varchar2(50))")
    print("table created successfully")
    assert True
    