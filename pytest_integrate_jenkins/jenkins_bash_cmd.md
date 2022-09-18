echo '### Traversing to the Test Directory ####'
cd %WORKSPACE%/..
echo '### Initializing the Virtual environment #### '
call ./env/Scripts/activate.bat
echo '### moving to the report directory ###'
cd %WORKSPACE%/Report
echo 'Executing the Test with Parameter #### '
call pytest -v ../test_login_data_drtiven_e2e.py --browser="%browser%" --html="%report%"