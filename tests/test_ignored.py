import pytest

@pytest.mark.skip(reason='no way of currently testing this')
class TestIgnoredClass:

    def DEV_T40_test_method1(self, record_property):
        record_property('testCaseKey', 'DEV-T40')
        assert 1 == 1

    def DEV_T41_test_method3(self):
        assert 5 == 4
