# Expected Type Decorator

Create a decorator `expected_type()` that checks if what the decorated function returns is of expected type. An `UnexpectedTypeException` should be raised if the type returned by the decorated function doesn't match the ones expected.

**Requirements:**

`expected_type()` should accept a tuple of many types that may be valid

`UnexpectedTypeException` should be raised if decorated function returns object of type that wasn't defined in expected_type()'s arguments (you have to implement that class)

`return_something` will be decorated with `expected_type` in the tests and will look exactly like in the example below

**Example:**

```python
@expected_type((str,))
def return_something(input):
    # do stuff here with the input...
    return something

>>> return_something('The quick brown fox jumps over the lazy dog.')
'The quick brown fox jumps over the lazy dog.' 

>>> return_something('The quick brown fox jumps over the lazy dog.')
'Maybe you'll output another string...'

>>> return_something(None)
UnexpectedTypeException: Was expecting instance of: str    <<< if the returned type isn't one of the expected ones.
```
