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

However, the JUnit automation endpoint relies on the specific format of naming tests - test case name is matched by full class name (or file path) and test method name or test case key is parsed from the method name if it starts with it or ends with it.
In order to mark a test with a test case key, it must be added at the end of the name. (Or the configuration of pytest framework might be adjusted, more information here: https://docs.pytest.org/en/stable/example/pythoncollection.html)

For example from TestClass:
```
class TestClass:

    # will match with test case with key DEV-T21
    def test_method_3_DEV_T21(self):
        assert 5 == 5

    # will match with test case named tests.test_sample.TestClass.test_method
    def test_method(self):
        x = 'this'
        assert 'h' in x


# will match with test case named tests.test_sample.test_method_1_without_class
def test_method_1_without_class():
    assert 1 == 1

```

### Execute tests in the example
In order to execute tests in the example on your local machine you’ll have to checkout this repository and install python 3 and pip. 
Next, install pytest `pip install pytest`. 
To use the code example, simply run `pyest` in the root folder. In order to generate junit format, use `pytest --junitxml=output/junitxml_report.xml`.
