import pytest

class TestClass:

    def DEV_T19_test_method_1(self, record_property):
        record_property('testCaseKey', 'DEV-T19')
        assert 1 == 1

    @pytest.mark.skip(reason='no way of currently testing this')
    def DEV_T20_test_method_2(self, record_property):
        record_property('testCaseKey', 'DEV-T20')
        assert 3 == 5

    def DEV_T21_test_method_3(self):
        assert 5 == 5

    def DEV_T22_test_method_4(self, record_property):
        record_property('testCaseKey', 'DEV-T19')
        x = 'this'
        assert 'h' in x


def DEV_T23_test_method_1_without_class(record_property):
    record_property('testCaseKey', 'DEV-T23')
    assert 1 == 1

def DEV_T24_test_method_2_without_class(record_property):
    record_property('testCaseKey', 'DEV-T24')
    assert 1 == 0