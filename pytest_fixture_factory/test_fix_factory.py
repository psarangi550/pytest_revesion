def test_foo(setup):
    get_list=setup("list")
    assert type(get_list)==list
    get_tup=setup("tuple")
    assert type(get_tup)==tuple
    
    
    