import pytest

@pytest.fixture(scope="class")
def setup():
    print("I am the first person")
    yield
    print("Successfully completed.")

def test_fixture_firstDemo(setup):
    print("Data get from the setup method to process")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    #data set seperately in Conftest.py file.
    return ["Chand", "Shaik", "rahulshettyacadamy.com"]

#How to run above testcase with multiple set of data in multiple runs

@pytest.fixture(params=[("Chrome", "Chand"), ("Firefox", "Shaik"), ("IE", "Shaik")])
def crossBrowser(request):
    return request.param    #here request = object
