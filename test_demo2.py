import pytest

#Mark only for Smoke & Regression Testing. This Annotation is used rarely.
@pytest.mark.smoke
@pytest.mark.skip
def test_firstname():
    print("My first name is Shaik")

@pytest.mark.smoke
def test_lastname():
    print("My last name is Chand")