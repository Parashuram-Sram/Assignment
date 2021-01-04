
Configuration:

1.Python and PIP needs to be installed before following below steps.

2.If Python is not installed, then download and install the latest version[Solution is created using 3.9 version] from https://www.python.org/downloads/

3.Check successfull installation by using commands: 1. python --version and 2. pip --version

Steps:

1. Download and Unzip(or clone the repository) the given "Assignment.zip" file at any drive say D:.

2. Go to unzipped folder "Assignment" i.e cd D:\Assignment

3. pip install -r requirements.txt

4. Configure the browser in BaseConfig.BROWSER . Currently CHROME and EDGE are supported.

5. Configure the city name in TestData.City_Name. If configured city name not present in the City_Id_Map, then please add the city with its id in the City_Id_Map
which is required for the API call. Or configure the city which is present in City_Id_Map for TestData.City_Name 

6. To run all tests,run the command : pytest Tests -n=3 --html=Report.html --disable-warnings

	6.a : -n=3 here implies parallel run. We are running 3 tests at time and can be changed.

7. To run only regression tests,run the command: pytest -m regression -n=2 --html=RegressionReports.html --disable-warnings

	7.a : Regression tests here implies the tests which are not mentioned in the given problem statement.

8. To run only feature tests,run the command: pytest -m feature -n=2 --html=FeatureReports.html --disable-warnings

	8.a: Feature tests here implies the tests which are asked to write in the given problem statement.

9. Open the reports html in any browser. D:\Assignment\Report.html

Note: There are few network related errors getting displayed on console. These errors are not harmful and are not affecting the test execution.I am in search
to make this off.