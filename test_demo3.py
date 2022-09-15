import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_Demo(self):
        print("Sample file1. ")
    def test_Demo1(self):
        print("Sample file2. ")
    def test_Demo2(self):
        print("Sample file3. ")
    def test_Demo3(self):
        print("Sample file4 is last file. ")