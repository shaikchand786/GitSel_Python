import pytest


def test_unit():
    print("Hello!")


@pytest.mark.xfail
def test_msg():
    message = "Hello"
    assert "Ho" in message


