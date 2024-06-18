from fuel import convert, gauge
import pytest

def test_convert_int():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("0/4") == 0

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_num_greater():
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_str():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(25) == '25%'
    assert gauge(75) == '75%'
    assert gauge(99) == 'F'

