import pytest

from pytestdemo.ClassLogDemo import baseclass


#@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("dataLoad")
class TextFix(baseclass):
    def test_datalog(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[1])
#       log.info("Successfully completed!")