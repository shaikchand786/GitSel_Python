import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("Test execution is completed!")


def test_fixtureDemo(setup):
    print("I will execute steps in fextureDemo method")