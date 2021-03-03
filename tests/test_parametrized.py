import pytest

@pytest.mark.parametrize('test_input,expected', [('3+5', 8), ('2+4', 7), ('6*9', 42)])
def DEV_T30_parametrized_test(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize('test_input,expected', [('3+5', 8), ('2+4', 7), ('6*9', 42)])
def DEV_T30_parametrized_test(test_input, expected, record_property):
    record_property('testCaseKey', 'DEV-T30')
    assert eval(test_input) == expected


@pytest.mark.skip(reason='require further analysis')
@pytest.mark.parametrize('test_input,expected', [('3+5', 8), ('2+4', 6), ('6*9', 42)])
def DEV_T32_parametrized_test(test_input, expected):
    assert eval(test_input) == expected


class ParametrizedTestClass:

    @pytest.mark.parametrize('test_input,expected', [('3+5', 8), ('2+4', 6), ('6*9', 42)])
    def DEV_T33_parametrized_test_in_class(test_input, expected, record_property):
        record_property('testCaseKey', 'DEV-T33')
        assert eval(test_input) == expected