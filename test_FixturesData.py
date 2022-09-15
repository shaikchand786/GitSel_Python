import pytest

from pytestdemo.ClassLogDemo import baseclass


@pytest.mark.usefixtures("dataLoad")
class TestEx2(baseclass):
    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        # bring all the selected data from conftest.py file and use in your web automation test
        log.info(dataLoad)
        log.info(dataLoad[1])


#How to derive parameterizations in fixtures
# def test_crossBrowser(crossBrowser):
#     print(crossBrowser[1])