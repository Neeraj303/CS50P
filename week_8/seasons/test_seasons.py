from seasons import get_minutes
import pytest
#import datetime


def test_cr_get_minutes():
    assert get_minutes("1998-03-19") == 13770720
    assert get_minutes("2024-05-24") == 0
    assert get_minutes("2000-01-15") == 12810240
    assert get_minutes("2024-01-01") == 207360

def test_inc_get_minutes():
    with pytest.raises(ValueError):
        get_minutes("1 Jan 1998")
    with pytest.raises(ValueError):
        get_minutes("January 1, 1999")
    with pytest.raises(ValueError):
        get_minutes("1908 Jan 1")

def test_inc_format_get_minutes():
    with pytest.raises(ValueError):
        get_minutes("1998/03/19")
    with pytest.raises(ValueError):
        get_minutes("1998/13/19")
    with pytest.raises(ValueError):
        get_minutes("1998 03 19")



