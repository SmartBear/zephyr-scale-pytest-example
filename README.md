# The exemplary configuration of pytest library to use its output in Zephyr Scale 

This is an example how to configure pytest library to generate output file that could be used as input for `/automations/executions/junit` endpoint.

### Configuration
The framework supports JUnitXml format out of the box. In order to generate file that is accepted by Zephyr Scale automation endpoint, it's sufficient to add the `--junitxml` option with the path of the output file, like  
`pytest --junitxml=output/junitxml_report.xml`. 

### Naming conventions
In the declared path or current directory, it searches for test_*.py or *_test.py files, imported by their test package name.
From those files, collect test items:
- `test` prefixed test functions or methods outside of class
- `test` prefixed test functions or methods inside `Test` prefixed test classes (without an __init__ method)
(https://docs.pytest.org/en/stable/goodpractices.html#test-discovery)

However, the JUnit automation endpoint relies on the specific format of naming tests - test case name is matched by test class name + test method name or test case key is parsed from the method name if it starts with it.
Those requirements might be at variance with the pytest conventions. 
It might be necessary to customize those rules in `pytest.ini` file to contain the `Test` or `test` word instead of starting with it. 
```
[pytest]
python_functions = *_test*
python_classes = *Test*
```

Overriding naming convention in `pytest.ini` does not include tests using `unittest.TestCase`. What is worse, it’s not allowed to use `record_property` fixture due to inheritance limits. However, there are two possible solution for this problem:
- override `testMethodPrefix` in `TestLoader`,
- allow custom marker by adding 
```
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        for marker in item.iter_markers(name="test_case_key"):
            test_case_key = marker.args[0]
            item.user_properties.append(("testCaseKey", test_case_key))
```
into `conftest.py` file (described in https://docs.pytest.org/en/stable/usage.html#record-property)
to later use it in the following way:
```
class TestStringMethods(unittest.TestCase):

    @pytest.mark.test_case_key('DEV-123')
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
```

