from ensurepip import version
import math_func
import pytest
import sys
@pytest.mark.skipif(sys.version_info < (3,3), reason='dont run this test')
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    print(math_func.add(7,3)), '---------------------------------'
@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) >= 14
    assert math_func.product(3) != 7
@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello ', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert "Heldlo" not in result
@pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello ' in result

def test_add_float():
    result = math_func.add(10.5, 25.5)
    assert result == 36

@pytest.mark.parametrize('arg1, arg2, result', 
        [
            (10.5, 25.5, 36),
            (7, 3, 10),
            ('Hello ', 'World', 'Hello World')
        ]           
        )       
def test_add(arg1, arg2, result):
    assert math_func.add(arg1, arg2) == result